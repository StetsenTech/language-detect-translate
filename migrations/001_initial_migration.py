"""Peewee migrations -- 001_initial_migration.py."""

import datetime as dt
import peewee as pw


def migrate(migrator, database, fake=False, **kwargs):
    """Migration that adds the translation table to database."""

    @migrator.create_model
    class Translations(pw.Model):
        text = pw.TextField(null=True)
        source_lanaguage = pw.TextField(null=True)
        target_language = pw.TextField(null=True)
        translated_text = pw.TextField(null=True)

        class Meta:
            db_table = "translations"



def rollback(migrator, database, fake=False, **kwargs):
    """Write your rollback migrations here."""

    migrator.remove_model('user_input')
