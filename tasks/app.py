"""Module handles tasks related to the general application"""
import os
from invoke import task

from lang_detect_translate.factory import create_app

@task
def run(config=None, port=None):
    """Runs an instance of application"""
    app = create_app(config)
    app.run(port=port)
