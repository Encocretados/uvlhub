from sqlalchemy import or_
import unidecode
from app.modules.dataset.models import Author, DSMetaData, DataSet, PublicationType, DSMetrics
from app.modules.featuremodel.models import FMMetaData, FeatureModel
from core.repositories.BaseRepository import BaseRepository
import re
from datetime import datetime

class ExploreRepository(BaseRepository):
    def __init__(self):
        super().__init__(DataSet)

    def filter(
        self, query="", sorting="newest", publication_type="any", tags=[],
        after_date=None, before_date=None,
        min_features=None, max_features=None, min_products=None, max_products=None,
        min_size=None, max_size=None, size_unit="KB", author_name="", **kwargs
    ):
        # Normaliza y limpia el texto de búsqueda
        normalized_query = unidecode.unidecode(query).lower()
        cleaned_query = re.sub(r'[,.":\'()\[\]^;!¡¿?]', "", normalized_query)
        tags = tags or []

        # Construye los filtros básicos de búsqueda a partir del query limpio
        filters = self.build_filters(cleaned_query)

        # Inicia la consulta con un outerjoin para no excluir datasets sin relaciones
        datasets = (
            self.model.query
            .join(DataSet.ds_meta_data)  # Mantén el join con DSMetaData
            .outerjoin(DSMetaData.authors)  # Cambiado a outerjoin para incluir datasets sin autores
            .outerjoin(DataSet.feature_models)  # Cambiado a outerjoin para incluir datasets sin modelos de características
            .outerjoin(FeatureModel.fm_meta_data)  # Cambiado a outerjoin
            .outerjoin(DSMetaData.ds_metrics)  # Cambiado a outerjoin
            .filter(DSMetaData.dataset_doi.isnot(None))  # Ignorar datasets sin DOI
        )

        print(f"Initial dataset count (no filters): {datasets.count()}")  # Log del número inicial de datasets

        # Filtra por el tipo de publicación
        if publication_type != "any":
            matching_type = next((member for member in PublicationType if member.value.lower() == publication_type), None)
            if matching_type is not None:
                datasets = datasets.filter(DSMetaData.publication_type == matching_type.name)
                print(f"After publication_type filter: {datasets.count()}")  # Log después del filtro de tipo de publicación

        # Aplica filtros basados en etiquetas
        if tags:
            datasets = datasets.filter(or_(*[DSMetaData.tags.ilike(f"%{tag}%") for tag in tags]))
            print(f"After tags filter: {datasets.count()}")  # Log después del filtro de etiquetas

        # Aplica filtro por autor
        if author_name:
            datasets = datasets.filter(or_(
                Author.name.ilike(f"%{author_name}%"),
                Author.affiliation.ilike(f"%{author_name}%"),
                Author.orcid.ilike(f"%{author_name}%")
            ))
            print(f"After author_name filter: {datasets.count()}")  # Log después del filtro de autor

        # Filtros relacionados con métricas de características y productos
        if min_features is not None:
            datasets = datasets.filter(DSMetrics.feature_count >= min_features)
            print(f"After min_features filter: {datasets.count()}")  # Log después del filtro de min_features
        if max_features is not None:
            datasets = datasets.filter(DSMetrics.feature_count <= max_features)
            print(f"After max_features filter: {datasets.count()}")  # Log después del filtro de max_features
        if min_products is not None:
            datasets = datasets.filter(DSMetrics.product_count >= min_products)
            print(f"After min_products filter: {datasets.count()}")  # Log después del filtro de min_products
        if max_products is not None:
            datasets = datasets.filter(DSMetrics.product_count <= max_products)
            print(f"After max_products filter: {datasets.count()}")  # Log después del filtro de max_products

        # Filtra por rango de fechas, si se proporcionan
        if after_date and before_date:
            datasets = datasets.filter(DataSet.created_at.between(after_date, before_date))
            print(f"After date range filter: {datasets.count()}")  # Log después del filtro de rango de fechas
        elif after_date:
            datasets = datasets.filter(DataSet.created_at >= after_date)
            print(f"After after_date filter: {datasets.count()}")  # Log después del filtro de after_date
        elif before_date:
            datasets = datasets.filter(DataSet.created_at <= before_date)
            print(f"After before_date filter: {datasets.count()}")  # Log después del filtro de before_date

        # Filtra por título y descripción si están presentes en la consulta
        if cleaned_query:
            datasets = datasets.filter(or_(*filters))
            print(f"After title and description filter: {datasets.count()}")  # Log después del filtro de título y descripción

        # Filtrar por tamaño
        if min_size:
            min_size = self.convert_to_bytes(min_size, size_unit)
        if max_size:
            max_size = self.convert_to_bytes(max_size, size_unit)

        # Filtro por tamaño en bytes
        if min_size:
            datasets = datasets.filter(DataSet.total_size_in_bytes >= min_size)
            print(f"After min_size filter: {datasets.count()}")  # Log después del filtro de min_size
        if max_size:
            datasets = datasets.filter(DataSet.total_size_in_bytes <= max_size)
            print(f"After max_size filter: {datasets.count()}")  # Log después del filtro de max_size

        # Ordenar los resultados por fecha de creación
        if sorting == "oldest":
            datasets = datasets.order_by(DataSet.created_at.asc())
        else:
            datasets = datasets.order_by(DataSet.created_at.desc())

        print(f"Final dataset count: {datasets.count()}")  # Log final después de aplicar todos los filtros

        # Retorna los datasets filtrados
        return datasets.all()

    def convert_to_bytes(self, size, unit):
        """Convierte el tamaño dado a bytes basado en la unidad."""
        size = float(size)
        unit = unit.lower()

        # Mapeo de unidades a multiplicadores en bytes
        unit_multipliers = {
            'b': 1,  # byte
            'kb': 1024,  # kilobyte
            'mb': 1024 ** 2,  # megabyte
            'gb': 1024 ** 3,  # gigabyte
            'tb': 1024 ** 4,  # terabyte
        }

        # Asegúrate de que la unidad esté bien definida
        if unit not in unit_multipliers:
            raise ValueError("Unidad de tamaño no válida.")

        return size * unit_multipliers[unit]

    def build_filters(self, cleaned_query):
        """Construye los filtros de búsqueda a partir del texto limpio"""
        filters = []
        for word in cleaned_query.split():
            filters.extend([
                DSMetaData.title.ilike(f"%{word}%"),
                DSMetaData.description.ilike(f"%{word}%"),
                Author.name.ilike(f"%{word}%"),
                Author.affiliation.ilike(f"%{word}%"),
                Author.orcid.ilike(f"%{word}%"),
                FMMetaData.uvl_filename.ilike(f"%{word}%"),
                FMMetaData.title.ilike(f"%{word}%"),
                FMMetaData.description.ilike(f"%{word}%"),
                FMMetaData.publication_doi.ilike(f"%{word}%"),
                FMMetaData.tags.ilike(f"%{word}%"),
                DSMetaData.tags.ilike(f"%{word}%"),
            ])
        return filters
