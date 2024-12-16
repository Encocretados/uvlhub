from app.modules.auth.models import User  
from app.modules.dataset.models import DSMetaData, DataSet
from app.modules.dataset.repositories import DataSetRepository, DSDownloadRecordRepository, DSViewRecordRepository
from app.modules.featuremodel.repositories import FeatureModelRepository  
from app import db  
from sqlalchemy import func  


class DashboardRepository:
    
    def __init__(self):
        self.dataset_repository = DataSetRepository()
        self.feature_model_repository = FeatureModelRepository()
        self.ds_download_record_repository = DSDownloadRecordRepository()
        self.ds_view_record_repository = DSViewRecordRepository()

    def get_total_datasets(self) -> int:
        """
        Obtiene el número total de datasets sincronizados.
        """
        return self.dataset_repository.count_synchronized_datasets()

    def get_total_feature_models(self) -> int:
        """
        Obtiene el número total de modelos de características.
        """
        return self.feature_model_repository.count_feature_models()

    def get_total_users(self) -> int:
        """
        Obtiene el número total de usuarios registrados.
        """
        return db.session.query(func.count(User.id)).scalar()
    
    # get_total_authors en el service
    
    def get_total_dataset_views(self) -> int:
        """
        Obtiene el número total de visualizaciones de datasets y modelos de características.
        """
        return self.ds_view_record_repository.total_dataset_views()

    def get_total_dataset_downloads(self) -> int:
        """
        Obtiene el número total de descargas de datasets y modelos de características.
        """
        dataset_downloads = self.ds_download_record_repository.total_dataset_downloads()
        return dataset_downloads

    def get_datasets_by_publication_type(self):
        """
        Devuelve un diccionario con el número de datasets agrupados por PublicationType.
        """
        result = db.session.query(
            DSMetaData.publication_type,
            func.count(DataSet.id)
        ).join(DataSet.ds_meta_data).group_by(DSMetaData.publication_type).all()

        return {row[0].value if row[0] else 'Unknown': row[1] for row in result}
    
    # get_total_feature_model_views en el service
    # get_total_feature_model_downloads en el service
    
    def get_total_feature_model_downloads(self) -> int:
        """
        Obtiene el número total de descargas de datasets y modelos de características.
        """
        dataset_downloads = self.ds_download_record_repository.total_dataset_downloads()
        return dataset_downloads

    # def get_average_dataset_rating(self) -> float:
    #     """
    #     Calcula la calificación promedio de todos los datasets.
    #     """
    #     avg_rating = db.session.query(func.avg(DatasetRating.rating)).scalar()
    #     return round(avg_rating, 1) if avg_rating is not None else 0.0

