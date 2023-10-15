import Task as t
import sqlite

class TaskStack:
    stack = []
    completed = []
    canceled = []

    @classmethod
    def removeTask(cls, task_id: str, completed: bool, canceled: bool):
        for task in TaskStack.stack:
            if task.id == task_id:
                cls.stack.remove(task)
                if completed:
                    TaskStack.completed.append(task)
                elif canceled:
                    TaskStack.canceled.append(task)

    @classmethod
    def appendTask(cls, task: t, completed: bool):
        if completed:
            cls.completed.append(task)
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
        for task in cls.canceled:
            counter += 1
            string += "~~Task " + str(counter) + "~~\n" + task.__str__()
        return string + "====^===="

    @classmethod
    def loadData(cls):
        stack_dict = sqlite.fetchData()
        cursor = sqlite.connect()

    @classmethod
    def saveData(cls):
        cursor = sqlite.connect()
        pass
