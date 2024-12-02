from datetime import datetime
from app import db


# Modelo User: Contiene información básica del usuario
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relación de uno a uno con UserProfile
    profile = db.relationship('UserProfile', backref='user', uselist=False)

    def __repr__(self):
        return f'<User {self.name}>'

# Modelo UserProfile: Contiene información adicional sobre el usuario
class UserProfile(db.Model):
    __tablename__ = 'user_profiles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)

    # Campos adicionales para el perfil
    orcid = db.Column(db.String(19))
    affiliation = db.Column(db.String(100))
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)

    # Método para guardar cambios
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<UserProfile {self.name} {self.surname}>'