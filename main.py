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
        case "completed":
            print(ts.TaskStack.getCompletedTasks())
