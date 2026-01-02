import sys
import math

from collections import defaultdict
from collections import deque
def load(vtype=int):
    return vtype(input().strip())
def load_list(seplator=" ", vtype=int):
    return [vtype(v) for v in input().strip().split(seplator)]

def notab(a, b):
    s = set((a,b))
    for c in "RGB":
        if c not in s:
            return c

n  = load()
s = list(load(str))

cntmap = dict()
for c in 'RGB':
    cnt = 0
    cntmap[c] = [0 for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        if s[i] == c:
            cnt += 1
        cntmap[c][i] = cnt

cnt = 0
for i in range(0, n):
    first = s[i]
    for j in range(i + 1, n):
        if s[j] == first:
            continue
        second = s[j]
        target = notab(first, second)
        if j+(j-i) < n and s[j+(j-i)] == target:
            cnt += cntmap[target][j+1] - 1
        else:
            cnt += cntmap[target][j+1] 
print(cnt)


