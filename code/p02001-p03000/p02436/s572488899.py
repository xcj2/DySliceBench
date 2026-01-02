def enqueue(t,x):
    list_t = list[t]
    list_t.append(x)
    return list

def front(t):
    list_t = list[t]
    if len(list_t)==0:
        return
    else:
        print(list_t[0])
        return list
def dequeue(t):
    list_t = list[t]
    if len(list_t) ==0:
        return
    else:
        del(list_t[0])
        return list
    
list1 = [int(i) for i in input().split()]
n = list1[0]
q = list1[1]

list=[]

for i in range(n):
    list_i = []
    list.append(list_i)

for i in range(q):
    list2 = [int(j) for j in input().split()]
    a = list2[0]
    if a == 0:
        t = list2[1]
        x = list2[2]
        enqueue(t,x)
    elif a ==1:
        t = list2[1]
        front(t)
    else :
        t = list2[1]
        dequeue(t)
