import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
n, m, x, y = M()
xlist = LI()
ylist = LI()
ans = 'War'
for i in range(-100, 101):
    if x < i and y >= i and max(xlist) < i and min(ylist) >= i:
        ans = 'No War'
        break
print(ans)