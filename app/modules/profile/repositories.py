from app.modules.profile.models import UserProfile
from core.repositories.BaseRepository import BaseRepository
from app.modules.auth.services import AuthenticationService



class UserProfileRepository(BaseRepository):
    def __init__(self):
        super().__init__(UserProfile)

    
    def get_user_profile():
       user = AuthenticationService().get_authenticated_user()   
       if user:
        return user.profile   
       return None
