import sys
stdin = sys.stdin

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from collections import deque

n = ni()
a = list(li())

ans = deque([])
for i, ai in enumerate(a):
    if i%2 == 0:
        ans.append(ai)
    else:
        ans.appendleft(ai)
        
if n%2 == 1:
    print(*list(ans)[::-1])
else:
    print(*list(ans))