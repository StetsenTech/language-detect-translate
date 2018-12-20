"""This module sets the defaults for application"""

DATABASE_URI = "sqlite:///lang_detect_translate.db"
DATABASE = {
    'name': 'lang_detect_translate.db',
    'engine': 'peewee.SqliteDatabase',
}

DEBUG = False
GCLOUD_AUTH = "gcloud_auth.json"