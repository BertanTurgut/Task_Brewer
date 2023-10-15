import sqlite3
import Task as t

def connect(db_name="task_essence"):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    return cursor

def closeConnection(cursor: sqlite3):
    cursor.close()

def createTable(cursor: sqlite3, table_name="tasks"):
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id text, importance int, end_date text, active int,"
                   " completed int, cancelled int, text text)")
    cursor.connection.commit()

def dropTable(cursor: sqlite3, table_name="tasks"):
    cursor.execute(f"DROP TABLE {table_name}")
    cursor.connection.commit()

def deleteTableData(cursor: sqlite3, table_name="tasks"):
    cursor.execute(f"DELETE FROM {table_name}")
    cursor.connection.commit()

def insertTask(cursor: sqlite3, task: t, table_name="tasks"):
    insert = f"INSERT INTO {table_name} VALUES (\"{task.id}\", {task.importance}, \"{task.end_date}\", {task.active}, " \
             f"{task.completed}, {task.cancelled}, \"{task.text}\")"
    cursor.execute(insert)
    cursor.connection.commit()

def updateTask(cursor: sqlite3, table_name: str, id: str, end_date: str, text: str, active: bool,
               completed: bool, cancelled: bool):
    active = 1 if active else 0
    completed = 1 if completed else 0
    cancelled = 1 if cancelled else 0
    update = f"UPDATE {table_name} SET end_date = \"{end_date}\", text = \"{text}\", active = {active}, " \
             f"completed = {completed}, cancelled = {cancelled} WHERE id = \"{id}\""
    cursor.execute(update)
    cursor.connection.commit()

def fetchData(cursor: sqlite3, table_name="tasks"):
    select = "SELECT * FROM {table_name} WHERE {status} ORDER BY id"
    stack_dict = dict()
    stack_dict["active"] = cursor.execute(select.format(table_name=table_name, status="active = 1")).fetchall()
    stack_dict["completed"] = cursor.execute(select.format(table_name=table_name, status="completed = 1")).fetchall()
    stack_dict["cancelled"] = cursor.execute(select.format(table_name=table_name, status="cancelled = 1")).fetchall()
    cursor.connection.commit()
    return stack_dict
