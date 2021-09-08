from app import db
from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    # id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # id = db.Column('id', db.Text(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), nullable = False)
    email = db.Column(db.String(60), index = True, unique= True, nullable = False)
    password = db.Column(db.String(250), nullable = False)
    level = db.Column(db.BigInteger, nullable = False)
    deleted_at = db.Column(db.DateTime, default = datetime.utcnow)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow)
    def __repr__(self) -> str:
        return f"<User {self}>"
    def set_password(self, password):
        self.password = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password, password)