from app.modules.dashboard.repositories import DashboardRepository
from app.modules.dataset.services import DataSetService
from app.modules.featuremodel.services import FeatureModelService
from core.services.BaseService import BaseService


class DashboardService(BaseService):

    def __init__(self):
        super().__init__(DashboardRepository())
        self.dataset_service = DataSetService()
        self.feature_model_service = FeatureModelService()

    def get_dashboard_data(self):
        return {
            "total_datasets": self.repository.get_total_datasets(),
            "total_features": self.repository.get_total_feature_models(),
            "total_users": self.repository.get_total_users(),
            "total_authors": self.dataset_service.count_authors(),
            # "average_rating": self.repository.get_average_dataset_rating(),
            "total_views": self.repository.get_total_dataset_views(),
            "total_downloads": self.repository.get_total_dataset_downloads(),
            "total_fm_views": self.feature_model_service.total_feature_model_views(),
            "total_fm_downloads": self.feature_model_service.total_feature_model_downloads(),
            "publication_type_data": self.repository.get_datasets_by_publication_type()
        }
