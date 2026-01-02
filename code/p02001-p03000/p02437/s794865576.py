import heapq

def insert(t, x):
    global Qlist
    heapq.heappush(Qlist[t], -x)

def getMax(t):
    global Qlist
    if Qlist[t]:
        num = Qlist[t][0]
        print(-num)

def deleteMax(t):
    global Qlist
    if Qlist[t]:
        heapq.heappop(Qlist[t])


Qlist = []
n,q  = map(int, input().split())

for i in range(n):
    Qi = []
    heapq.heapify(Qi)
    Qlist.append(Qi)

for i in range(q):
    queryi = list(map(int, input().split()))

    if queryi[0] == 0:
        insert(queryi[1], queryi[2])
    
    elif queryi[0] == 1:
        getMax(queryi[1])

    else:
        deleteMax(queryi[1])
    
