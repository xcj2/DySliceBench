def examB():
    from collections import deque
    Sa = S(); Sb = S(); Sc = S();
    Sa = deque(Sa); Sb = deque(Sb); Sc = deque(Sc);
    cur = "a"
    while (True):
        if cur=="a":
            if Sa:
                cur = Sa.popleft()
            else:
                ans = "A"
                break
        if cur=="b":
            if Sb:
                cur = Sb.popleft()
            else:
                ans = "B"
                break
        if cur=="c":
            if Sc:
                cur = Sc.popleft()
            else:
                ans = "C"
                break
    print(ans)

import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examB()
