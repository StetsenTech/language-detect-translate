"""Module contains the base for all schemata"""
from flask_marshmallow import Marshmallow

marsh = Marshmallow()

class BaseSchema(marsh.Schema):
    """Base schema"""
