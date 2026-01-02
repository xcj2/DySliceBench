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

H,W,M = LI()
h,w = LIR(M,2)

c = [0]*W
r = [0]*H

d = defaultdict(int)
for i in range(M):
    r[h[i]-1] += 1
    c[w[i]-1] += 1
    d[(h[i]-1,w[i]-1)] = 1

max_c = -1
c_index = []
max_r = -1
r_index = []

for i in range(H):
    if r[i] > max_r:
        max_r = r[i]
        r_index = [i]
    elif r[i] == max_r:
        r_index.append(i)
    else:
        continue

for i in range(W):
    if c[i] > max_c:
        max_c = c[i]
        c_index = [i]
    elif c[i] == max_c:
        c_index.append(i)
    else:
        continue

ans = max_c+max_r
flag = False
for i in r_index:
    for j in c_index:
        if d[(i,j)] == 0:
            flag = True
            break
    if flag:
        break

if not flag:
    ans -= 1

print(ans)