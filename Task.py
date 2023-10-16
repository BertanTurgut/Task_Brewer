import time
import datetime
import Task_Stack as ts
import sqlite

class Task:
    def __init__(self, database_fetch: bool, end_date: str, text: str, importance=1, id="", active=False,
                 completed=False, cancelled=False):
        self.importance = importance
        self.end_date = end_date
        self.text = text
        if database_fetch:
            self.id = id
            self.active = active
            self.completed = completed
            self.cancelled = cancelled
        else:
            self.id = Task.idFormatter(str(datetime.datetime.now())[:21])
            self.active = True
            self.completed = False
            self.cancelled = False
        ts.TaskStack.appendTask(self, self.completed, self.cancelled)
        time.sleep(0.1)

    @staticmethod
    def fetchFromDatabase(cursor: sqlite):
        stack_dict = sqlite.fetchData(cursor)
        for data_list in stack_dict.values():
            for data_tuple in data_list:
                Task(True, data_tuple[2], data_tuple[6], data_tuple[1], data_tuple[0], data_tuple[3], data_tuple[4],
                     data_tuple[5])

    def completeAccess(self, id: str, end_date: str, text: str, importance: int, active: bool, completed: bool,
                 cancelled: bool):
        self.id = id
        self.importance = importance
        self.end_date = end_date
        self.text = text
        self.active = active
        self.completed = completed
        self.cancelled = cancelled
        pass

    def complete(self):
        self.completed = True
        self.deactivate()

    def cancel(self):
        self.cancelled = True
        self.deactivate()

    def deactivate(self):
        self.active = False
        ts.TaskStack.removeTask(self.id, self.completed, self.cancelled)

    def stateControl(self):
        pass

    def edit(self, end_date: str, text: str, importance: int):
        if end_date == "-":
            end_date = self.end_date
        self.end_date = end_date
        if text == "-":
            text = self.text
        self.text = text
        if importance == 0:
            importance = self.importance
        self.importance = importance

    def __str__(self):
        string = "ID: " + self.id + "\nImportance: " + str(self.importance) + "\nEnd Date: " + self.end_date + \
                 "\nActive: " + str(self.active) + "\nCompleted: " + str(self.completed) + "\nCancelled: " + \
                 str(self.cancelled) + "\nText: \"" + self.text + "\"\n"
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
