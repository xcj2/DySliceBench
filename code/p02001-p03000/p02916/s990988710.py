import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
n = I()
A = LI()
B = LI()
C = LI()
ans = 0
before = -1
for i in range(n):
    taberuNo = A[i]-1
    ans += B[taberuNo]
    if taberuNo -1 == before and i != 0:
        ans += C[before]
    before = taberuNo
print(ans)