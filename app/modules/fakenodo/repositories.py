from app import db
from app.modules.fakenodo.models import Fakenodo
from core.repositories.BaseRepository import BaseRepository


class FakenodoRepository(BaseRepository):
    def __init__(self):
        super().__init__(Fakenodo)  # Initialize with Fakenodo model

    def create_new_fakenodo(self, meta_data=None, doi=None):
        """
        Create a new fakenodo (deposition) with metadata and optionally a DOI.

        Args:
            meta_data (dict): The metadata for the fakenodo.
            doi (str): The DOI for the fakenodo (optional).

        Returns:
            Fakenodo: The created fakenodo object.
        """
        if meta_data is None:
            meta_data = {}  # Default empty dictionary if no metadata provided

        fakenodo = Fakenodo(meta_data=meta_data, doi=doi)
        db.session.add(fakenodo)
        db.session.commit()
        return fakenodo
