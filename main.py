import Task as t
import Task_Stack as ts

t1 = t.Task("start", "end", "text")
t2 = t.Task("", "", "text")
print(ts.TaskStack.__str__())