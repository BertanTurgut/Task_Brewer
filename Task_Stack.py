import Task as t

class TaskStack:
    stack = []

    @classmethod
    def removeTask(cls, task_id: str):
        for task in TaskStack.stack:
            if task.id == task_id:
                cls.stack.remove(task)

    @classmethod
    def appendTask(cls, task: t):
        cls.stack.append(task)

    @classmethod
    def __str__(cls):
        string = "=====\n"
        counter = 0
        for task in cls.stack:
            counter += 1
            string += "~Task " + str(counter) + "~\n" + task.__str__()
        return string + "====="
