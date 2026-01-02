from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
a = [inpl() for i in range(n)]
a.sort(key=lambda x:x[1])
a.sort()
z = []
# pprint.pprint(a)
for i in range(n):
    for j in range(i,n):
        if i == j:
            continue
        z.append((a[i][0]-a[j][0], a[i][1]-a[j][1]))
c = Counter(z)
# pprint.pprint(c)
if n == 1:
    print(1)
else:
    print(n-c.most_common()[0][1])
# print(n-c.most_common()[0][1])

