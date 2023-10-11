import Task_Stack as ts
import datetime

class Task:
    def __init__(self, start_date: str, end_date: str, text: str, importance=1, active=True):
        self.id = str(datetime.datetime.now())[:19]
        self.importance = importance
        self.end_date = end_date
        self. active = active
        self.text = text

        ts.TaskStack.stack.append(self)

    def remove(self):
        ts.TaskStack.removeTask(self.id)
        pass

    def __str__(self):
        string = "ID: " + self.id + "\nImpotance: " + str(self.importance) + "\nStart Date: " + "\nEnd Date: " + \
                 self.end_date + "\nActive: " + str(self.active) + "\nText: " + self.text + "\n"
        return string
