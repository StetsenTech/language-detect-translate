from invoke import Collection
from . import app, db

namespace = Collection(app, db)