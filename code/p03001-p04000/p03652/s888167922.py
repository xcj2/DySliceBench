import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N,num):
    if N<=0:
        return [[]]*num
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

from collections import Counter

N,M = II()
A = []
for _ in range(N):
    A.append(III())

used = [False]*(M+1)
place = [0]*N
elements = [0]*N
for i in range(N):
    elements[i] = A[i][0]

ans = float('inf')
for i in range(M):
    c = Counter(elements)
    val = c.most_common(1)[0][0]
    num = c.most_common(1)[0][1]
    if num<ans:
        ans = num
    used[val] = True
    index_list = []
    for j,e in enumerate(elements):
        if e==val:
            index_list.append(j)
    for index in index_list:
        for p in range(place[index],M):
            if used[A[index][p]]:
                continue
            else:
                elements[index] = A[index][p]
                place[index] = p+1
                break

print(ans)