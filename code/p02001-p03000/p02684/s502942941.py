def Int():
    return int(input())
def Ints():
    return map(int,input().split())
def IntList():
    return list(Ints())
def IntMat(N):
    return [IntList() for i in range(N)]

import sys
sys.setrecursionlimit(4100000)
rl = sys.stdin.readline

N,K = Ints()
A = IntList()
visited = {}

Nex = [1]
now = 1
now = A[now-1]
visited[1] = 1

toS = 1

while 1:
    if not now in visited:
        if toS==K:
            print(now)
            sys.exit()
        visited[now] = 1
        now = A[now-1]
        toS += 1
    else:
        start = now
        break
    
Nex = [start]
now = start
now = A[now-1]
while now != start:
    Nex.append(now)
    now = A[now-1]    

L = len(Nex)
d = toS-L

#print(Nex)
#print(toS)
#print(toS-L)

print(Nex[(K-d)%L])