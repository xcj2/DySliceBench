from collections import deque

def enqueue(t, x):
    global Qlist
    Qlist[t].appendleft(x)

def front(t):
    global Qlist
    if Qlist[t] != deque():
        print(Qlist[t][-1])

def dequeue(t):
    global Qlist
    if Qlist[t] != deque():
        Qlist[t].pop()


n, q = map(int, input().split())
Qlist =[]
for i in range(n):
    Q = deque()
    Qlist.append(Q)

for j in range(q):
    queryi = list(map(int, input().split()))
    
    if queryi[0] == 0:
        enqueue(queryi[1], queryi[2])

    elif queryi[0] == 1:
        front(queryi[1])

    else: 
        dequeue(queryi[1])
