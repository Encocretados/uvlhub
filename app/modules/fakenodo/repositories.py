from app.modules.fakenodo.models import Deposition
from core.repositories.BaseRepository import BaseRepository


class DepositionRepo(BaseRepository):
    def __init__(self):
        super().__init__(Deposition)

    def create_new_deposition(self, dep_metadata):
        return self.create(dep_metadata=dep_metadata)