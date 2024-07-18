# service.TaskService.py
from models.TaskModel import TaskModel
def CreateTask(name, description):
    task = TaskModel.create(task_name = name, task_description = description, is_active = True)
def GetTasks():
    tasks = TaskModel.select()
    return tasks
def ToggleTask(task_id):
    task = TaskModel.get(TaskModel.task_id == task_id)
    task.is_active = not task.is_active
    task.save()

