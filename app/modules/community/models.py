from app import db

class Community(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    members = db.relationship('User', secondary='community_members', back_populates='communities', cascade='all, delete')
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
