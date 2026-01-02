
from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())


ans = 0
M = inp()
zan = []
for m in range(M):
    d,c = inpl()

    while True:
        if c == 1:
            zan.append(d)
            break
        elif c%2 == 0:
            if d == 0:
                ans += c
                break
            elif d <= 4:
                ans += c//2
                d *= 2
                c //= 2
            else:
                ans += c
                d = d*2 - 9
                c //= 2
        else:
            zan.append(d)
            c -= 1

zan.reverse()

bx = zan[0]
for x in zan[1:]:
    d = x + bx
    if d >= 10:
        bx = d - 10 + 1
        ans += 2
    else:
        bx = d
        ans += 1

print(ans)
