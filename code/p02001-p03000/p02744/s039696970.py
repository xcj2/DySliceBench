import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

N = I()

S = [[0]]
ans = []
while S:
    v = S.pop()
    if len(v) == N:
        ans.append(v)
        continue
    else:
        for u in range(max(v)+2):
            S.append(v+[u])

for i,a in enumerate(ans):
    a = list(map(lambda x: chr(x+ord('a')),a))
    ans[i] = ''.join(a)

ans.sort()

for a in ans:
    print(a)