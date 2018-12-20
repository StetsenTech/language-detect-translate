"""Module handles tasks related to the database"""
from invoke import task
from playhouse.db_url import connect
from peewee_migrate import Router

from lang_detect_translate.factory import create_app

@task
def migrate(config=None):
    """Runs migration for project"""
    app = create_app(config)

    db = connect(app.config['DATABASE_URI'])
    router = Router(db)
    router.run()
