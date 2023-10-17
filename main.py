import datetime
import Task as t
import Task_Stack as ts
import sqlite
import help

print("===============")
print("= Task Brewer =")
print("===============\n")
cursor = sqlite.connect()
sqlite.createTable(cursor)
unnoticed_misses = 0
try:
    print("Fetching")
    t.Task.fetchFromDatabase(cursor)
    print("Fetch successful\n")
except:
    print("[!] Fetch unsuccessful\n")
cnt = True
if unnoticed_misses == 1:
    print("[!] 1 task is missed since last entry\n")
elif unnoticed_misses > 1:
    print(f"[!] {unnoticed_misses} tasks are missed since last entry\n")
while cnt:
    command = input("Enter command: ")
    match command:
        case "help":
            print(help.helpString("main"))
        case "exit":
            print("\nSaving stacks")
            try:
                ts.TaskStack.saveTaskStacks(cursor)
                print("Saved stacks\n")
                print("Exiting program")
                cnt = False
            except:
                print("[!] Save unsuccessful")
                command = input("Exit anyways?")
                match command:
                    case "yes":
                        cnt = False
                        print("\nExiting program")
                    case _:
                        pass
        case "exit without save":
            cnt = False
            print("\nExiting program")
        case "active":
            print(ts.TaskStack.getActiveTasks(True))
            inActive = True
            while inActive:
                command = input("Enter command in actives: ")
                match command:
                    case "help":
                        print(help.helpString("actives"))
                    case "edit task":
                        try:
                            number = int(input("Task number: "))
                            print("~~Task " + str(number) + "~~\n" + ts.TaskStack.stack[number - 1].strCommonView())
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
                            print("~~Task " + str(number) + "~~\n" + ts.TaskStack.stack[number - 1].strCommonView())
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
                            print("~~Task " + str(number) + "~~\n" + ts.TaskStack.stack[number - 1].strCommonView())
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
                        print(ts.TaskStack.getActiveTasks(True))
                    case "search":
                        searched_str = input("Searched string: ")
                        candidates = ts.TaskStack.searchTask(searched_str, True)
                        if candidates.__len__() == 0:
                            print("Couldn't find any matching tasks")
                        else:
                            print(f"Found {candidates.__len__()} matching active tasks: ")
                            string = "====v====\n"
                            i = 1
                            for task in candidates:
                                string += task.__str__() + "------\n" if i < candidates.__len__() else task.__str__()
                                i += 1
                            string += "====^===="
                            print(string)
                    case "exit":
                        inActive = False
        case "completed":
            print(ts.TaskStack.getCompletedTasks(True))
        case "cancelled":
            print(ts.TaskStack.getCancelledTasks(True))
        case "missed":
            print(ts.TaskStack.getMissedTasks(True))
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
        case "search":
            searched_str = input("Searched string: ")
            candidates = ts.TaskStack.searchTask(searched_str)
            if candidates.__len__() == 0:
                print("Couldn't find any matching tasks")
            else:
                print(f"Found {candidates.__len__()} matching tasks: ")
                string = "====v====\n"
                i = 1
                for task in candidates:
                    string += task.__str__() + "------\n" if i < candidates.__len__() else task.__str__()
                    i += 1
                string += "====^===="
                print(string)
        case "search in active":
            searched_str = input("Searched string: ")
            candidates = ts.TaskStack.searchTask(searched_str, True)
            if candidates.__len__() == 0:
                print("Couldn't find any matching active tasks")
            else:
                print(f"Found {candidates.__len__()} matching active tasks: ")
                string = "====v====\n"
                i = 1
                for task in candidates:
                    string += task.__str__() + "------\n" if i < candidates.__len__() else task.__str__()
                    i += 1
                string += "====^===="
                print(string)
        case "search in completed":
            searched_str = input("Searched string: ")
            candidates = ts.TaskStack.searchTask(searched_str, False, True)
            if candidates.__len__() == 0:
                print("Couldn't find any matching completed tasks")
            else:
                print(f"Found {candidates.__len__()} matching completed tasks: ")
                string = "====v====\n"
                i = 1
                for task in candidates:
                    string += task.__str__() + "------\n" if i < candidates.__len__() else task.__str__()
                    i += 1
                string += "====^===="
                print(string)
        case "search in cancelled":
            searched_str = input("Searched string: ")
            candidates = ts.TaskStack.searchTask(searched_str, False, False, True)
            if candidates.__len__() == 0:
                print("Couldn't find any matching cancelled tasks")
            else:
                print(f"Found {candidates.__len__()} matching cancelled tasks: ")
                string = "====v====\n"
                i = 1
                for task in candidates:
                    string += task.__str__() + "------\n" if i < candidates.__len__() else task.__str__()
                    i += 1
                string += "====^===="
                print(string)
        case "search in missed":
            searched_str = input("Searched string: ")
            candidates = ts.TaskStack.searchTask(searched_str, False, False, False, True)
            if candidates.__len__() == 0:
                print("Couldn't find any matching missed tasks")
            else:
                print(f"Found {candidates.__len__()} matching missed tasks: ")
                string = "====v====\n"
                i = 1
                for task in candidates:
                    string += task.__str__() + "------\n" if i < candidates.__len__() else task.__str__()
                    i += 1
                string += "====^===="
                print(string)
