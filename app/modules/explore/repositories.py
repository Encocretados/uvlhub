import re
from datetime import datetime

import unidecode
from sqlalchemy import or_

from app.modules.dataset.models import (Author, DataSet, DSMetaData, DSMetrics,
                                        PublicationType)
from app.modules.featuremodel.models import FeatureModel, FMMetaData
from core.repositories.BaseRepository import BaseRepository


class ExploreRepository(BaseRepository):
    def __init__(self):
        super().__init__(DataSet)

    def filter(
        self,
        query="",
        sorting="newest",
        publication_type="any",
        tags=[],
        after_date=None,
        before_date=None,
        min_size=None,
        max_size=None,
        size_unit="KB",
        author_name=None,
        **kwargs,
    ):
        # Normaliza y limpia el texto de búsqueda
        normalized_query = unidecode.unidecode(query).lower()
        cleaned_query = re.sub(r'[,.":\'()\[\]^;!¡¿?]', "", normalized_query)
        tags = tags or []

        # Construye los filtros básicos de búsqueda a partir del query limpio
        filters = self.build_filters(cleaned_query)

        # Inicia la consulta con un outerjoin para no excluir datasets sin relaciones
        datasets = (
            self.model.query.join(DataSet.ds_meta_data)  # Mantén el join con DSMetaData
            .outerjoin(
                DSMetaData.authors
            )  # Cambiado a outerjoin para incluir datasets sin autores
            .outerjoin(
                DataSet.feature_models
            )  # Cambiado a outerjoin para incluir datasets sin modelos de características
            .outerjoin(FeatureModel.fm_meta_data)  # Cambiado a outerjoin
            .outerjoin(DSMetaData.ds_metrics)  # Cambiado a outerjoin
            .filter(DSMetaData.dataset_doi.isnot(None))  # Ignorar datasets sin DOI
        )

        print(
            f"Initial dataset count (no filters): {datasets.count()}"
        )  # Log del número inicial de datasets

        # Filtra por el tipo de publicación
        if publication_type != "any":
            matching_type = next(
                (
                    member
                    for member in PublicationType
                    if member.value.lower() == publication_type
                ),
                None,
            )
            if matching_type is not None:
                datasets = datasets.filter(
                    DSMetaData.publication_type == matching_type.name
                )
                print(
                    f"After publication_type filter: {datasets.count()}"
                )  # Log después del filtro de tipo de publicación

        # Aplica filtros basados en etiquetas
        if tags:
            datasets = datasets.filter(
                or_(*[DSMetaData.tags.ilike(f"%{tag}%") for tag in tags])
            )
            print(
                f"After tags filter: {datasets.count()}"
            )  # Log después del filtro de etiquetas

        # Filtra por autor si se proporciona
        if author_name:
            datasets = datasets.filter(Author.name.ilike(f"%{author_name}%"))
            print(
                f"After author filter: {datasets.count()}"
            )  # Log después del filtro de autor

        # Ordena los resultados por fecha de creación
        if sorting == "oldest":
            datasets = datasets.order_by(DataSet.created_at.asc())
        else:
            datasets = datasets.order_by(DataSet.created_at.desc())

        print(
            f"Final dataset count: {datasets.count()}"
        )  # Log final después de aplicar todos los filtros

        # Filtra por rango de fechas, si se proporcionan
        if after_date and before_date:
            datasets = datasets.filter(
                DataSet.created_at.between(after_date, before_date)
            )
            print(
                f"After date range filter: {datasets.count()}"
            )  # Log después del filtro de rango de fechas
        elif after_date:
            datasets = datasets.filter(DataSet.created_at >= after_date)
            print(
                f"After after_date filter: {datasets.count()}"
            )  # Log después del filtro de after_date
        elif before_date:
            datasets = datasets.filter(DataSet.created_at <= before_date)
            print(
                f"After before_date filter: {datasets.count()}"
            )  # Log después del filtro de before_date

        # Filtra por título y descripción si están presentes en la consulta
        if cleaned_query:
            datasets = datasets.filter(or_(*filters))
            print(
                f"After title and description filter: {datasets.count()}"
            )  # Log después del filtro de título y descripción

        def safe_convert_to_float(value):
            try:
                return float(value)
            except (ValueError, TypeError):
                return None

        # Filtrado por tamaño (en KB, pero puede ser convertido a bytes si es necesario)
        def convert_to_bytes(size: float, unit: str):
            if size is None:
                return None
            if unit == "bytes":
                return size
            elif unit == "KB":
                return size * 1024
            elif unit == "MB":
                return size * 1024 * 1024
            elif unit == "GB":
                return size * 1024 * 1024 * 1024
            return None  # Manejo por defecto si la unidad es desconocida

        # Convertir tamaños mínimos y máximos a números válidos antes de pasarlos
        min_size = safe_convert_to_float(min_size)
        max_size = safe_convert_to_float(max_size)

        # Convertir tamaños a bytes según la unidad
        min_size = (
            convert_to_bytes(min_size, size_unit) if min_size is not None else None
        )
        max_size = (
            convert_to_bytes(max_size, size_unit) if max_size is not None else None
        )

        # Depuración
        print(
            f"Min Size: {min_size} bytes, Max Size: {max_size} bytes, Size Unit: {size_unit}"
        )

        # Obtener todos los resultados y filtrar por tamaño usando get_file_total_size()
        # Después de la consulta inicial y la ordenación:
        filtered_datasets = []
        for dataset in datasets.all():
            # Obtener el tamaño total usando el método definido
            total_size = dataset.get_file_total_size()

            # Asegúrate de que los datos se impriman para depuración
            print(f"Dataset ID: {dataset.id}, Total size: {total_size} bytes")

            # Validar el rango del tamaño
            if min_size is not None and total_size <= min_size:
                print(f"Excluido por ser menor al mínimo ({min_size} bytes).")
                continue
            if max_size is not None and total_size >= max_size:
                print(f"Excluido por ser mayor al máximo ({max_size} bytes).")
                continue

            # Si pasa las condiciones, añadirlo a la lista final
            filtered_datasets.append(dataset)

        # Imprimir resumen del filtrado
        print(f"Total datasets mostrados: {len(filtered_datasets)}")

        for Dataset in datasets:
            print("Total size: " + str(Dataset.get_file_total_size()))

        return filtered_datasets

    def build_filters(self, cleaned_query):
        """Construye los filtros de búsqueda a partir del texto limpio"""
        filters = []
        for word in cleaned_query.split():
            filters.extend(
                [
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
                ]
            )
        return filters
