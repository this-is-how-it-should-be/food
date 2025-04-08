from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class Food(db.Model, SerializerMixin):
    __tablename__ = 'foods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    restaurant = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    google_maps_link = db.Column(db.String, nullable=False)
    yelp_link = db.Column(db.String, nullable=False)

    @validates('name', 'image', 'description', 'restaurant', 'address', 'google_maps_link', 'yelp_link')
    def validate_string_columns(self, key, value):
        if not (type(value) == str):
            raise TypeError(f"{key} must be a string!")
        elif len(value) == 0:
            raise ValueError(f"{key} must be at least 1 character long!")
        else:
            return value