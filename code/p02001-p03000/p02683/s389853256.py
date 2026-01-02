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

N,M,X = Ints()
C = []
A = []

for i in range(N):
    In = IntList()
    C.append(In[0])
    A.append(In[1:])
    
ans = 10**16

import itertools

for i in itertools.product([0,1], repeat=N):
    Now = [0]*M
    tmpans = 0
    for j in range(N):
        if i[j]==1:
            tmpans += C[j]
            for k in range(M):
                Now[k] += A[j][k]
    if min(Now) >= X:
        ans = min(ans,tmpans)
        
if ans==10**16:
    print(-1)
else:
    print(ans)