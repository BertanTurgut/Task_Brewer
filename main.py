import datetime
import Task as t
import Task_Stack as ts
import sqlite

print("===============")
print("= Task Brewer =")
print("===============\n")
cursor = sqlite.connect()
sqlite.createTable(cursor)
try:
    print("Fetching")
    t.Task.fetchFromDatabase(cursor)
    print("Fetch successful\n")
except:
    print("Fetch unsuccessful\n")
cnt = True
while cnt:
    command = input("Enter command: ")
    match command:
        case "exit":
            print("\nSaving stacks")
            try:
                ts.TaskStack.saveTaskStacks(cursor)
                print("Saved stacks")
                print("Exiting program")
                cnt = False
            except:
                print("Save unsuccessful")
                command = input("Exit anyways?")
                match command:
                    case "yes":
                        cnt = False
                        print("Exiting program")
                    case _:
                        pass
        case "active":
            print(ts.TaskStack.getActiveTasks())
            inActive = True
            while inActive:
                command = input("Enter command in actives: ")
                match command:
                    case "edit task":
                        try:
                            number = int(input("Task number: "))
                            print("~~Task " + str(number) + "~~\n" + ts.TaskStack.stack[number - 1].__str__())
                            deadline = str(input("End Date: "))
                            if deadline == "-":
                                pass
                            else:
                                formatted_deadline = deadline.replace(".", "")
                                i = 0
                                for index in formatted_deadline:
                                    if t.Task.compareStringNumbers(index,
                                                                   (str(datetime.datetime.now())).replace("-", "")[i]) \
                                            == -1:
                                        raise Exception
                                    elif t.Task.compareStringNumbers(index, (str(datetime.datetime.now()))
                                                                     .replace("-", "")[i]) == 1:
                                        break
                                    i += 1
                            text = str(input("Text: "))
                            importance = int(input("Importance: "))
                            save = input("Approve? ")
                            match save:
                                case "yes":
                                    ts.TaskStack.stack[number - 1].edit(deadline, text, importance)
                                case "no":
                                    pass
                                case _:
                                    raise Exception
                        except:
                            print("Invalid demand")
                    case "complete task":
                        try:
                            number = int(input("Task number: "))
                            print("~~Task " + str(number) + "~~\n" + ts.TaskStack.stack[number - 1].__str__())
                            save = input("Approve? ")
                            match save:
                                case "yes":
                                    ts.TaskStack.stack[number - 1].complete()
                                case "no":
                                    pass
                                case _:
                                    raise Exception
                        except:
                            print("Invalid demand")
                    case "cancel task":
                        try:
                            number = int(input("Task number: "))
                            print("~~Task " + str(number) + "~~\n" + ts.TaskStack.stack[number - 1].__str__())
                            save = input("Approve? ")
                            match save:
                                case "yes":
                                    ts.TaskStack.stack[number - 1].cancel()
                                case "no":
                                    pass
                                case _:
                                    raise Exception
                        except:
                            print("Invalid demand")
                    case "list":
                        print(ts.TaskStack.getActiveTasks())
                    case "exit":
                        inActive = False
        case "completed":
            print(ts.TaskStack.getCompletedTasks())
        case "cancelled":
            print(ts.TaskStack.getCancelledTasks())
        case "missed":
            print(ts.TaskStack.getMissedTasks())
        case "add task":
            try:
                deadline = str(input("End Date: "))
                formatted_deadline = deadline.replace(".", "")
                i = 0
                for index in formatted_deadline:
                    if t.Task.compareStringNumbers(index,
                                                   (str(datetime.datetime.now())).replace("-", "")[i]) == -1:
                        raise Exception
                    elif t.Task.compareStringNumbers(index,
                                                     (str(datetime.datetime.now())).replace("-", "")[i]) == 1:
                        break
                    i += 1
                text = str(input("Text: "))
                importance = int(input("Importance: "))
                save = input("Approve? ")
                match save:
                    case "yes":
                        task = t.Task(False, deadline, text, importance)
                    case "no":
                        pass
                    case _:
                        raise Exception
            except:
                print("Invalid demand")
