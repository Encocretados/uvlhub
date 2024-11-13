import logging

from flask import render_template

from app.modules.featuremodel.services import FeatureModelService
from app.modules.public import public_bp
from app.modules.dataset.services import DataSetService, SizeService

logger = logging.getLogger(__name__)


@public_bp.route("/")
def index():
    logger.info("Access index")
    dataset_service = DataSetService()
    feature_model_service = FeatureModelService()

    # Statistics: total datasets and feature models
    datasets_counter = dataset_service.count_synchronized_datasets()
    feature_models_counter = feature_model_service.count_feature_models()

    # Statistics: total downloads
    total_dataset_downloads = dataset_service.total_dataset_downloads()
    total_feature_model_downloads = feature_model_service.total_feature_model_downloads()

    # Statistics: total views
    total_dataset_views = dataset_service.total_dataset_views()
    total_feature_model_views = feature_model_service.total_feature_model_views()
    total_popular_datasets = dataset_service.get_popular_datasets()

    # Statistics: total size of all datasets
    total_datasets = dataset_service.get_all_datasets()
    total_size = sum(dataset.get_file_total_size() for dataset in total_datasets)
    total_size = SizeService().get_human_readable_size(total_size)
    datasets_dict = [dataset.to_dict() for dataset in total_datasets]

    return render_template(
        "public/index.html",
        datasets=dataset_service.latest_synchronized(),
        datasets_counter=datasets_counter,
        feature_models_counter=feature_models_counter,
        total_dataset_downloads=total_dataset_downloads,
        total_feature_model_downloads=total_feature_model_downloads,
        total_dataset_views=total_dataset_views,
        total_feature_model_views=total_feature_model_views,
        datasets_dict=datasets_dict,
        total_dataset_size=total_size,
        total_popular_datasets=total_popular_datasets 
    )