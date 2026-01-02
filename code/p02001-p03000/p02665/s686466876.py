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
mod = 10**9+7

N = Int()
A = IntList()

tmp = 0

for i in range(N+1):
    tmp += A[i]*2**(N-i)
    
if tmp > 2**N:
    print(-1)
    sys.exit()
    
if N==0:
  print(1)
  sys.exit()


B = A[::-1]
ans = 1
par = 1
C = []
MAXpar = B[0]

for i in range(N):
    leaf = B[i]
    if len(C)>=1:
        MINP = C[-1][0]
        MAXP = C[-1][1]
        C.append([(MINP+leaf+1)//2,MAXP+leaf])
    else:
        C.append([(leaf+1)//2,leaf])
        

D = C[::-1]
#print(D)
for i in range(1,N):
    minp,maxp = D[i]
    
    ans += A[i]+min(maxp,2*par-A[i])
    #print(A[i],min(maxp,2*par-A[i]))
    par = min(maxp,2*par-A[i])
    
ans += A[-1]
print(ans)
    