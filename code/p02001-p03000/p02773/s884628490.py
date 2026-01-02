import sys
import math
from collections import defaultdict

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
S = []
for i in range(N):
    S.append(str(input()))

d = defaultdict(int)
for i in range(N):
    d[S[i]] += 1

k = 0
ans = []
for x in d.items():
    if x[1] > k:
        k = x[1]
        ans = [x[0]]
    elif x[1] == k:
        ans.append(x[0])
    else:
        pass

ans.sort()
for a in ans:
    print(a)
