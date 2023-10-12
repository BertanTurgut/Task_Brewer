import time

import Task_Stack as ts
import datetime

class Task:
    def __init__(self, end_date: str, text: str, importance=1):
        self.id = Task.idFormatter(str(datetime.datetime.now())[:21])
        self.importance = importance
        self.end_date = end_date
        self.active = True
        self.completed = False
        self.canceled = False
        self.text = text

        ts.TaskStack.appendTask(self, self.completed)

        time.sleep(0.1)

    def complete(self):
        self.completed = True
        self.deactivate()

    def cancel(self):
        self.canceled = True
        self.deactivate()

    def deactivate(self):
        self.active = False
        ts.TaskStack.removeTask(self.id, self.completed, self.canceled)

    def __str__(self):
        string = "ID: " + self.id + "\nImportance: " + str(self.importance) + "\nEnd Date: " + self.end_date + \
                 "\nActive: " + str(self.active) + "\nCompleted: " + str(self.completed) + "\nCancelled: " + \
                 str(self.canceled) + "\nText: " + self.text + "\n"
        return string

    def __lt__(self, other):
        i = 0
        for index in self.id:
            match Task.compareStringNumbers(index, other.id[i]):
                case 1:
                    return True
                case 0:
                    pass
                case -1:
                    return False
            i += 1
        return False

    def __gt__(self, other):
        i = 0
        for index in self.id:
            match Task.compareStringNumbers(index, other.id[i]):
                case 1:
                    return False
                case 0:
                    pass
                case -1:
                    return True
            i += 1
        return False

    @staticmethod
    def compareStringNumbers(first: str, second: str):
        digits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
        index_f = digits.index(first)
        index_s = digits.index(second)
        if index_f > index_s:
            return 1
        elif index_f == index_s:
            return 0
        elif index_f < index_s:
            return -1

    @staticmethod
    def idFormatter(raw_id: str):
        formatted_id = raw_id.replace("-", "")
        formatted_id = formatted_id.replace(" ", "")
        formatted_id = formatted_id.replace(":", "")
        formatted_id = formatted_id.replace(".", "")
        return formatted_id
