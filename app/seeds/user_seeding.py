from flask_seeder import Seeder, Faker, generator
from app.model.user import User
from werkzeug.security import generate_password_hash
import os
class DemoSeeder(Seeder):
  # run() will be called by Flask-Seeder
  def run(self):
    # Create a new Faker and tell it how to create User objects
    faker = Faker(
      cls=User,
      init={
        "id": generator.Sequence(),
        "name": generator.Name(),
        "email": generator.Email(),
        "level": 1,
        "password": generate_password_hash(str(os.environ.get("DB_DATABASE", "")))
      }
    )

    # Create 5 users
    for user in faker.create(5):
      print("Adding user: %s" % user)
      self.db.session.add(user)
      # self.db.session.commit()
