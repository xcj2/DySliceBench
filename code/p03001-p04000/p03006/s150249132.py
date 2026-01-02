import sys
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return int(input())
from collections import defaultdict, Counter
import bisect

sys.setrecursionlimit(10000000)

n = SI()
xy = [(0,0) for _ in range(n)]
div = defaultdict(int)
for i in range(n):
    x, y = LI()
    xy[i] = (x, y)
if n==1:
    print(1)
else:
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            else:
                div["{}_{}".format(xy[i][0] - xy[j][0], xy[i][1]- xy[j][1])] += 1

    max_ = max(div.values())
    print(n - max_)