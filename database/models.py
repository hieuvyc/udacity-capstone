from sqlalchemy import Column, String, Integer, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

db = SQLAlchemy()

Base = declarative_base()

def setup_db(app, database_path):
    """Setup the database connection"""
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)
    db.init_app(app)
    return db

class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    release_date = Column(Date, nullable=False)

    def insert(self):
        """Insert a new record into the database"""
        db.session.add(self)
        db.session.commit()

    def update(self):
        """Update an existing record in the database"""
        db.session.commit()

    def delete(self):
        """Delete a record from the database"""
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "title": self.title,
            "release_date": self.release_date.strftime("%Y-%m-%d"),
        }

class Actor(db.Model):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)

    def insert(self):
        """Insert a new record into the database"""
        db.session.add(self)
        db.session.commit()

    def update(self):
        """Update an existing record in the database"""
        db.session.commit()

    def delete(self):
        """Delete a record from the database"""
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
        }

# Load environment variables from .env file
load_dotenv()

database_name = os.getenv('DATABASE_NAME')
database_user = os.getenv('DATABASE_USER')
database_password = os.getenv('DATABASE_PASSWORD')
database_host = os.getenv('DATABASE_HOST')
database_path = (
    f'postgresql://{database_user}:{database_password}@{database_host}/'
    f'{database_name}'
)
engine = create_engine(database_path)
Base.metadata.create_all(engine)