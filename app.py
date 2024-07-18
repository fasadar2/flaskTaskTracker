#app.py


#Функция демонстрации работы тегов шаблона
# @app.route("/", methods = ['get','post'])
# def index():
#     numbers = ["Первый", "Второй", "Третий", "Четвертый"]
#     if request.method == 'POST':
#         name = request.form.get('name')
#
#         return render_template('index.html', message=name, arr=numbers
#         )
#     return render_template('index.html', message="Hello Flask", arr=numbers)
from flask import Flask, render_template,request, redirect,url_for
from service.TaskService import ToggleTask,GetTasks,CreateTask
app = Flask(__name__)
@app.route("/task")
def get_tasks(): #Просмотр задач
    tasks = GetTasks()
    return render_template('index.html',tasks = tasks)
@app.route('/toggle/<int:task_id>')
def toggle_task(task_id): #Переключение состояния
    ToggleTask(task_id)
    return redirect(url_for('get_tasks'))
@app.route("/add-new",methods =["get","post"])
def add_task(): #Добавление задачи
    if request.method == "POST":

        name = request.form.get('name')
        description = request.form.get('description')

        CreateTask(name,description)
        return redirect(url_for('get_tasks'))
    return render_template('add-new-task.html')

if __name__ == '__main__':
    app.run(debug=True)

