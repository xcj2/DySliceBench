import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
N = I()
A = LI()
ans = A[0]
if 0 in A:
    ans = 0
else:
    for i in range(1, N):
        if ans > 10**18:
            ans = -1
            break
        else:
            ans = ans*A[i]
if ans > 10**18:
    ans = -1
print(ans)