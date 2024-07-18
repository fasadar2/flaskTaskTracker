#models.TaskModel
from models.BaseModel import BaseModel
from peewee import PrimaryKeyField,TextField,BooleanField

class TaskModel(BaseModel):
    task_id = PrimaryKeyField(column_name="task_id")
    task_name = TextField(column_name="task_name")
    task_description = TextField(column_name="task_description")
    is_active = BooleanField(column_name="is_active")
    class Meta:
        table_name = "task"