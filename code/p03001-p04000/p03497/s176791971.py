import sys,collections
from collections import deque
from operator import itemgetter
sys.setrecursionlimit(10**7)
def Is(): return [int(x) for x in sys.stdin.readline().split()]
def Ss(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

n,k = Is()
a = Is()
d = collections.defaultdict(int)
for i in range(len(a)):
    d[a[i]] += 1 
dl = sorted(list(d.items()),key=itemgetter(1))
ans = 0
for i in range(len(dl)):
    if len(d) <= k:
        break
    ans += dl[i][1]
    del d[dl[i][0]]
print(ans)