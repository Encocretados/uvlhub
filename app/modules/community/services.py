from app import db
from app.modules.community.models import Community
from app.modules.community.repositories import CommunityRepository
from core.services.BaseService import BaseService


class CommunityService(BaseService):
    def __init__(self):
        self.repository = CommunityRepository()
        super().__init__(self.repository)

    def get_all_by_user(self, user):
        return self.repository.get_all_by_user(user)

    def create_community(self, data):
        name = data.get("name")
        description = data.get("description")
        user = data.get("user")
        # Crear la comunidad
        community = Community(name=name, description=description, creator_id=user.id)
        # Asociar el usuario creador con la comunidad
        community.members.append(user)
        # Guardar en la base de datos
        db.session.add(community)
        try:
            db.session.commit()
            return {"success": True, "community": community}
        except Exception as e:
            db.session.rollback()
            return {"success": False, "error": str(e)}
