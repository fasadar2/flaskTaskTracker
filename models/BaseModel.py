#models.BaseModel
from peewee import Model
from db_config import db


class BaseModel(Model):
    class Meta:
        database = db
