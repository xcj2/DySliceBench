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

s = deque(lc())
lens = len(s)

ok = True
ans = 0

while len(s):
    if len(s) == 1:
        s.pop()
    
    elif s[0] == s[-1]:
        s.pop()
        s.popleft()
        
    else:
        if s[0] == "x":
            s.append("x")
            ans += 1
        elif s[-1] == "x":
            s.appendleft("x")
            ans += 1
        else:
            ok = False
            break
    
if ok:
    print(ans)
else:
    print(-1)