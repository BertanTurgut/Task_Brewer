import Task as t
import sqlite

class TaskStack:
    stack = []
    completed = []
    cancelled = []
    missed = []

    @classmethod
    def removeTask(cls, task_id: str, completed: bool, canceled: bool, missed: bool):
        for task in TaskStack.stack:
            if task.id == task_id:
                cls.stack.remove(task)
                if completed:
                    TaskStack.completed.append(task)
                elif canceled:
                    TaskStack.cancelled.append(task)
                elif missed:
                    TaskStack.missed.append(task)

    @classmethod
    def appendTask(cls, task: t, completed: bool, cancelled: bool, missed: bool):
        if completed:
            cls.completed.append(task)
        elif cancelled:
            cls.cancelled.append(task)
        elif missed:
            cls.missed.append(task)
        else:
            cls.stack.append(task)

    @classmethod
    def getActiveTasks(cls):
        string = "====v====\n"
        counter = 0
        for task in cls.stack:
            counter += 1
            string += "~~Task " + str(counter) + "~~\n" + task.__str__()
        return string + "====^===="

    @classmethod
    def getCompletedTasks(cls):
        string = "====v====\n"
        counter = 0
        for task in cls.completed:
            counter += 1
            string += "~~Task " + str(counter) + "~~\n" + task.__str__()
        return string + "====^===="

    @classmethod
    def getCancelledTasks(cls):
        string = "====v====\n"
        counter = 0
        for task in cls.cancelled:
            counter += 1
            string += "~~Task " + str(counter) + "~~\n" + task.__str__()
        return string + "====^===="

    @classmethod
    def getMissedTasks(cls):
        string = "====v====\n"
        counter = 0
        for task in cls.missed:
            counter += 1
            string += "~~Task " + str(counter) + "~~\n" + task.__str__()
        return string + "====^===="

    @classmethod
    def saveTaskStacks(cls, cursor: sqlite):
        sqlite.deleteTableData(cursor)
        for active in cls.stack:
            sqlite.insertTask(cursor, active)
        for completed in cls.completed:
            sqlite.insertTask(cursor, completed)
        for cancelled in cls.cancelled:
            sqlite.insertTask(cursor, cancelled)
        for missed in cls.missed:
            sqlite.insertTask(cursor, missed)

    @classmethod
    def stateControlTaskStacks(cls, cursor: sqlite):
        pass