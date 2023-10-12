import Task as t
import Task_Stack as ts

print("===============")
print("= Task Brewer =")
print("===============\n")
cnt = True
while cnt:
    command = input("Enter command: ")
    match command:
        case "exit":
            cnt = False
        case "active":
            print(ts.TaskStack.getActiveTasks())
            inActive = True
            while (inActive):
                command = input("Enter command in actives: ")
                match command:
                    case "complete task":
                        try:
                            index = int(input("Task index: "))
                            ts.TaskStack.stack[index].complete()
                        except:
                            print("Invalid demand")
                    case "cancel task":
                        try:
                            index = int(input("Task index: "))
                            ts.TaskStack.stack[index].cancel()
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
        case "add task":
            try:
                deadline = str(input("End Date: "))
                text = str(input("Text: "))
                importance = int(input("Importance: "))
                task = t.Task(deadline, text, importance)
            except:
                print("Invalid demand")
