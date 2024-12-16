import logging
from datetime import datetime, timezone
import logging
from app.modules.community.models import Community
from flask_login import current_user
from typing import Optional

from flask_login import current_user
from sqlalchemy import desc, func

from app.modules.dataset.models import (Author, DataSet, DOIMapping,
                                        DSDownloadRecord, DSMetaData,
                                        DSViewRecord)
from core.repositories.BaseRepository import BaseRepository

logger = logging.getLogger(__name__)


class AuthorRepository(BaseRepository):
    def __init__(self):
        super().__init__(Author)


class DSDownloadRecordRepository(BaseRepository):
    def __init__(self):
        super().__init__(DSDownloadRecord)

    def total_dataset_downloads(self) -> int:
        max_id = self.model.query.with_entities(func.max(self.model.id)).scalar()
        return max_id if max_id is not None else 0


class DSMetaDataRepository(BaseRepository):
    def __init__(self):
        super().__init__(DSMetaData)

    def filter_by_doi(self, doi: str) -> Optional[DSMetaData]:
        return self.model.query.filter_by(dataset_doi=doi).first()


class DSViewRecordRepository(BaseRepository):
    def __init__(self):
        super().__init__(DSViewRecord)

    def total_dataset_views(self) -> int:
        max_id = self.model.query.with_entities(func.max(self.model.id)).scalar()
        return max_id if max_id is not None else 0

    def the_record_exists(self, dataset: DataSet, user_cookie: str):
        return self.model.query.filter_by(
            user_id=current_user.id if current_user.is_authenticated else None,
            dataset_id=dataset.id,
            view_cookie=user_cookie,
        ).first()

    def create_new_record(self, dataset: DataSet, user_cookie: str) -> DSViewRecord:
        return self.create(
            user_id=current_user.id if current_user.is_authenticated else None,
            dataset_id=dataset.id,
            view_date=datetime.now(timezone.utc),
            view_cookie=user_cookie,
        )


class DataSetRepository(BaseRepository):
    def __init__(self):
        super().__init__(DataSet)

    def get_synchronized(self, current_user_id: int) -> DataSet:
        return (
            self.model.query.join(DSMetaData)
            .filter(
                DataSet.user_id == current_user_id, DSMetaData.dataset_doi.isnot(None)
            )
            .order_by(self.model.created_at.desc())
            .all()
        )

    def get_unsynchronized(self, current_user_id: int) -> DataSet:
        return (
            self.model.query.join(DSMetaData)
            .filter(
                DataSet.user_id == current_user_id, DSMetaData.dataset_doi.is_(None)
            )
            .order_by(self.model.created_at.desc())
            .all()
        )

    def get_unsynchronized_dataset(
        self, current_user_id: int, dataset_id: int
    ) -> DataSet:
        return (
            self.model.query.join(DSMetaData)
            .filter(
                DataSet.user_id == current_user_id,
                DataSet.id == dataset_id,
                DSMetaData.dataset_doi.is_(None),
            )
            .first()
        )

    def count_synchronized_datasets(self):
        return (
            self.model.query.join(DSMetaData)
            .filter(DSMetaData.dataset_doi.isnot(None))
            .count()
        )

    def count_unsynchronized_datasets(self):
        return (
            self.model.query.join(DSMetaData)
            .filter(DSMetaData.dataset_doi.is_(None))
            .count()
        )

    def latest_synchronized(self):
        return (
            self.model.query.join(DSMetaData)
            .filter(DSMetaData.dataset_doi.isnot(None))
            .order_by(desc(self.model.id))
            .limit(5)
            .all()
        )

    def synchronize_unsynchronized_datasets(
        self, current_user_id: int, dataset_id: int
    ) -> None:
        # Obtener los datasets no sincronizados para el usuario y filtrarlos por datasetId si es necesario
        unsynchronized_datasets = self.get_unsynchronized(current_user_id)

        # Si deseas solo sincronizar un dataset específico, filtra usando el datasetId
        dataset = next((d for d in unsynchronized_datasets if d.id == dataset_id), None)

        if dataset:
            # Lógica para sincronizar el dataset
            dataset.ds_meta_data.dataset_doi = self.generate_doi_for_dataset(dataset)
            self.session.commit()  # usa self.session para hacer commit
        else:
            raise ValueError("Dataset no encontrado.")

    def generate_doi_for_dataset(self, dataset: DataSet) -> str:
        # Genera un DOI para el dataset (esto depende de tu implementación)
        return f"10.1234/dataset/{dataset.id}"

    def get_all(self):
        return self.model.query.all()


class DOIMappingRepository(BaseRepository):
    def __init__(self):
        super().__init__(DOIMapping)

    def get_new_doi(self, old_doi: str) -> str:
        return self.model.query.filter_by(dataset_doi_old=old_doi).first()
