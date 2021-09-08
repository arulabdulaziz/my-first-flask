from app import db
from datetime import datetime
from app.model.lecturer import Lecturer
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nim = db.Column(db.String(30), nullable = False)
    name = db.Column(db.String(250), nullable = False)
    phone = db.Column(db.String(15), nullable = False)
    address = db.Column(db.String(250), nullable = False)
    first_lecturer = db.Column(db.BigInteger, db.ForeignKey(Lecturer.id))
    second_lecturer = db.Column(db.BigInteger, db.ForeignKey(Lecturer.id))
    deleted_at = db.Column(db.DateTime, default = datetime.utcnow)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow)
    def __repr__(self) -> str:
        return f"<Student {self.name}>"