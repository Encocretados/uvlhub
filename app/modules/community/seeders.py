from app.modules.community.models import Community
from app.modules.auth.models import User
from core.seeders.BaseSeeder import BaseSeeder

class CommunitySeeder(BaseSeeder):

    priority = 1  # High priority

    def run(self):

        communities = [
            Community(name='community1', description='Community 1 description'),
            Community(name='community2', description='Community 2 description'),
        ]

        seeded_communities = self.seed(communities)

        users = User.query.limit(2).all()
        if users:
            for community in seeded_communities:
                community.members.extend(users)
                self.db.session.commit()
            self.db.session.commit()