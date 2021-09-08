from app import db
from datetime import datetime

class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    title = db.Column(db.String(250), nullable = False)
    path = db.Column(db.String(250), nullable = False)
    deleted_at = db.Column(db.DateTime, default = datetime.utcnow)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow)
    def __repr__(self) -> str:
        return f"<Image {self.title}>"