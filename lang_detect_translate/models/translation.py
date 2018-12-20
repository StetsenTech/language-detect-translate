"""Model responsible for querying the translation table"""
from base import BaseModel
from peewee import TextField

class Translation(BaseModel):
    """Model class for the translations table"""
    input = TextField()
    target_language = TextField()
    target_language = TextField()
    translated_text = TextField()
