from flask import Flask;
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder
from flask_jwt_extended import JWTManager
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# from app.seeds.user_seeding import DemoSeeder
# seeder = FlaskSeeder()
# seeder.init_app(app, db)
# def seed_db():
#     result = DemoSeeder
#     return result.run
# app.cli.add_command(seed_db)

from app.model import user, lecturer, student
from app import routes
