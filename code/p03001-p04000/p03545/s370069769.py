def examC():
    ABCD = S()
    loop = 2**3
    for i in range(loop):
        cur = int(ABCD[0])
        for j in range(3):
            if (i>>j)&1==1:
                cur += int(ABCD[j+1])
            else:
                cur -= int(ABCD[j+1])
        if cur==7:
            cur = i
            break
    ans = str(ABCD[0])
    for i in range(3):
        if (cur>>i)&1 == 1:
            ans += "+"
        else:
            ans += "-"
        ans += str(ABCD[i+1])
    ans += "=7"
    print(ans)

import sys,copy,bisect,itertools
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC()
