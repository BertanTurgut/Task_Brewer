import sqlite3
import Task as t
import Task_Stack as t_s

def connect():
    db = sqlite3.connect("task_essence")
    cursor = db.cursor()
    return cursor

create_table = "CREATE TABLE IF NOT EXISTS tasks (id varchar, importance int, end_date varchar, active int, " \
               "completed int, cancelled int, text text)"

def insertTask(task: t.Task):
    pass

def updateTask(task: t.Task):
    pass

def fetchData():
    pass