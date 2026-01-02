from collections import deque

def insert(t, x):
    Llist[t].append(x)

def dump(t):
    print(*Llist[t])


def splice(s, t):
    if Llist[t]:
        if len(Llist[t]) ==1:
            Llist[s].appendleft(Llist[t][0])
            Llist[t] = Llist[s]
        elif len(Llist[s]) == 1:
            Llist[t].append(Llist[s][0])
        else:   
            Llist[t].extend(Llist[s])
    else:
        Llist[t] = Llist[s]

    Llist[s] = deque() 

n, q = map(int, input().split())

Llist = []

for i in range(n):
    Llist.append(deque())

for i in range(q):
    queryi = list(map(int, input().split()))

    if queryi[0] == 0:
        insert(queryi[1], queryi[2])
    
    elif queryi[0] == 1:
        dump(queryi[1])
    
    else:
        splice(queryi[1], queryi[2])
