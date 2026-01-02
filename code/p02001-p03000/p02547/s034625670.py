import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
n = I()
ans = 'No'
cnt = 0
for i in range(n):
    a, b = M()
    if a == b:
        cnt += 1
        if cnt == 3:
            ans = 'Yes'
            break
    else:
        cnt = 0
print(ans)