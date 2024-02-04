# TEST DATA: tasks = [['A',1,10,100,'y'],['B',2,17,19,'n'],['C',2,12,27,'y'],['D',7,18,25,'n'],['E',1,10,15,'y']]
# tasks = [name,completion_time,deadline,importance:1(highest)-10(lowest),urgency:'y','n']

tasks=[['A',1,10,4,'n'],['B',3,17,5,'y'],['C',1,12,6,'n'],['D',4,18,1,'y']]
sorted_urgent_tasks=[]
sorted_not_urgent_tasks=[]

max_deadline = tasks[0][2]
for i in range(len(tasks)):
    if tasks[i][4] == 'y':
        sorted_urgent_tasks.append(tasks[i])
    else:
        sorted_not_urgent_tasks.append(tasks[i])
    if tasks[i][2] > max_deadline:
        max_deadline = tasks[i][2]

sorted_urgent_tasks.sort(key = lambda x: x[3])
sorted_not_urgent_tasks.sort(key = lambda x: x[3])
sorted_urgent_tasks.extend(sorted_not_urgent_tasks)
min_deadline = 9
print("Urgent tasks based on increasing order of importance: ",sorted_urgent_tasks)
print("Maximum deadline is ",max_deadline)

# calculate slots assuming work hours start from 9 am and end at 6 pm
available_slots =[]
for i in range(min_deadline,max_deadline):
    available_slots.append([i,i+1])

# allotting slots
# considering a task can be completed in parts and either entire or no task is completed in the given deadline
l = len(available_slots)
print("Available slots: ", available_slots)
for i in range(len(sorted_urgent_tasks)):
    sorted_urgent_tasks[i].append([])
    task_time = sorted_urgent_tasks[i][1]
    task_deadline = sorted_urgent_tasks[i][2]
    count_hrs = 0
    index_task_deadline = -1
    if max_deadline < task_deadline:
        count_hrs = len(available_slots)
    elif ([task_deadline - 1, task_deadline] not in available_slots):
        for slot in (available_slots):
            if (slot[1] <= task_deadline):
                count_hrs += 1
                index_task_deadline = available_slots.index(slot)
    else:
        for slot in (available_slots):
            if (slot[1] == task_deadline):
                index_task_deadline = available_slots.index(slot)
                for slot in range(index_task_deadline, - 1, -1):
                    count_hrs += 1
    if not (l):
        break
    elif (count_hrs < task_time):
        continue
    else:
        print('\nFor task ',sorted_urgent_tasks[i][0],':')
        min_deadline = available_slots[0][0]
        if max_deadline <= task_deadline:
            for slot in range(task_time):
                sorted_urgent_tasks[i][-1].append(available_slots[l-1])
                available_slots.remove(available_slots[l-1])
                l = len(available_slots)
        # print("Urgent tasks based on increasing order of importance: ", sorted_urgent_tasks)
        else:
            for time in range(max_deadline,min_deadline,-1):
                if time > task_deadline:
                    continue
                else:
                    if index_task_deadline != -1:
                        for slot in range(task_time):
                            sorted_urgent_tasks[i][-1].append(available_slots[index_task_deadline])
                            available_slots.remove(available_slots[index_task_deadline])
                            l = len(available_slots)
                            index_task_deadline -= 1
                        break
                    break
    if l > 0:
        max_deadline = available_slots[l - 1][1]
    print("Available slots after alloting: ", available_slots)
for i in range(i+1,len(sorted_urgent_tasks)):
    sorted_urgent_tasks[i].append([])
    sorted_urgent_tasks[i][5] = sorted_urgent_tasks[i][::-1]
for i in range(i,-1,-1):
    sorted_urgent_tasks[i][5] = sorted_urgent_tasks[i][5][::-1]
print("\nTO DO LIST:")
for task_no,task in enumerate(sorted_urgent_tasks):
    print(task_no+1,task[0],"-----Allotted slot(s): ",task[-1])
