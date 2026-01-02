import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
N = I()
pl = LI()
ans = 0
for i in range(2, N):
    p1 = pl[i-2]
    p2 = pl[i-1]
    p3 = pl[i]
    temp = list()
    temp.append(p1)
    temp.append(p2)
    temp.append(p3)
    temp.sort()
    if temp[1] == p2:
        ans += 1
print(ans)