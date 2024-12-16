from app.modules.auth.models import User
from app.modules.community.models import Community
from core.seeders.BaseSeeder import BaseSeeder


class CommunitySeeder(BaseSeeder):

    priority = 1  # High priority

    def run(self):
        # No crear comunidades
        communities = []  # No se crean comunidades

        # No hacer nada con los usuarios si no hay comunidades
        # La parte del código que gestiona a los miembros también se puede dejar vacía
        users = User.query.limit(2).all()
        if users:
            # No se hace nada con los usuarios ya que no hay comunidades
            pass

        # Si se desea, se puede dejar el commit, pero no es necesario si no hay cambios
        self.db.session.commit()
