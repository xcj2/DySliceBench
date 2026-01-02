from collections import deque

def push(t, x):
    global Slist
    Slist[t].append(x)

def top(t):
    global Slist
    if Slist[t] != deque():
        print(Slist[t][-1])

def pop(t):
    global Slist
    if Slist[t] != deque():
        Slist[t].pop()
    


n, q = map(int, input().split())
Slist =[]
for i in range(n):
    S = deque()
    Slist.append(S)

for j in range(q):
    queryi = list(map(int, input().split()))
    
    if queryi[0] == 0:
        push(queryi[1], queryi[2])

    elif queryi[0] == 1:
        top(queryi[1])

    else: 
        pop(queryi[1])
