from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
mod2 = 998244353
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n,a,b,c,d = inpl()
s = input()
def chk(i):
    if s[i] == s[i+1] == '#':
        print('No')
        quit()
    return True
def cc(i):
    if s[i] == s[i+1] == s[i+2] == '.':
        return True
    return False

if c < d:
    for i in range(b-1,d-1):
        chk(i)
    for i in range(a-1,c-1):
        chk(i)
else:
    for i in range(b-2,d-1):
        if cc(i):
            break
    else:
        print('No')
        quit()
    for i in range(a-1,c-1):
        chk(i)
print('Yes')