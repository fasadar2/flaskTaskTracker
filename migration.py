# migration.py
from models.TaskModel import TaskModel
if __name__ == "__main__":
    TaskModel.drop_table()
    TaskModel.create_table()
