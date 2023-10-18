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
    def getActiveTasks(cls, common_view: bool = False):
        string = "====v====\n"
        counter = 0
        for task in cls.stack:
            counter += 1
            if common_view:
                string += "~~Task " + str(counter) + "~~\n" + task.strCommonView()
            else:
                string += "~~Task " + str(counter) + "~~\n" + task.__str__()
        return string + "====^===="

    @classmethod
    def getCompletedTasks(cls, common_view: bool = False):
        string = "====v====\n"
        counter = 0
        for task in cls.completed:
            counter += 1
            if common_view:
                string += "~~Task " + str(counter) + "~~\n" + task.strCommonView()
            else:
                string += "~~Task " + str(counter) + "~~\n" + task.__str__()
        return string + "====^===="

    @classmethod
    def getCancelledTasks(cls, common_view: bool = False):
        string = "====v====\n"
        counter = 0
        for task in cls.cancelled:
            counter += 1
            if common_view:
                string += "~~Task " + str(counter) + "~~\n" + task.strCommonView()
            else:
                string += "~~Task " + str(counter) + "~~\n" + task.__str__()
        return string + "====^===="

    @classmethod
    def getMissedTasks(cls, common_view: bool = False):
        string = "====v====\n"
        counter = 0
        for task in cls.missed:
            counter += 1
            if common_view:
                string += "~~Task " + str(counter) + "~~\n" + task.strCommonView()
            else:
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
    def searchTask(cls, searched_str: str, active: bool = False, completed: bool = False, cancelled: bool = False,
                   missed: bool = False):
        lowered = searched_str.lower()
        candidate_list = []
        if active:
            for task in cls.stack:
                try:
                    if task.text.lower().find(lowered) != -1:
                        candidate_list.append(task)
                except:
                    pass
        elif completed:
            for task in cls.completed:
                try:
                    if task.text.lower().find(lowered) != -1:
                        candidate_list.append(task)
                except:
                    pass
        elif cancelled:
            for task in cls.cancelled:
                try:
                    if task.text.lower().find(lowered) != -1:
                        candidate_list.append(task)
                except:
                    pass
        elif missed:
            for task in cls.missed:
                try:
                    if task.text.lower().find(lowered) != -1:
                        candidate_list.append(task)
                except:
                    pass
        else:
            for task in cls.stack:
                try:
                    if task.text.lower().find(lowered) != -1:
                        candidate_list.append(task)
                except:
                    pass
            for task in cls.completed:
                try:
                    if task.text.lower().find(lowered) != -1:
                        candidate_list.append(task)
                except:
                    pass
            for task in cls.cancelled:
                try:
                    if task.text.lower().find(lowered) != -1:
                        candidate_list.append(task)
                except:
                    pass
            for task in cls.missed:
                try:
                    if task.text.lower().find(lowered) != -1:
                        candidate_list.append(task)
                except:
                    pass
        return candidate_list

