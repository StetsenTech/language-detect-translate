"""Module contains the base configurations for models"""

from playhouse.flask_utils import FlaskDB

db = FlaskDB()

class BaseModel(db.Model):
    """Base model that sets up db interactions"""
