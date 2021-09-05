from app import db
from datetime import datetime

class Lecturer(db.Model):
    __tablename__ = 'lecturers'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nidn = db.Column(db.String(30), nullable = False)
    name = db.Column(db.String(250), nullable = False)
    phone = db.Column(db.String(15), nullable = False)
    address = db.Column(db.String(250), nullable = False)
    deleted_at = db.Column(db.DateTime, default = datetime.utcnow)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow)
    def __repr__(self) -> str:
        return f"<Lecturer {self.name}>"