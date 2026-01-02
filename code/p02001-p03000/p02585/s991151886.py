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

N,K = LI()
P = LI()
C = LI()

for i in range(N):
    P[i] -= 1

# 何回で自分に戻ってくるか
ret = [0]*N
for i in range(N):
    p = i
    c = 1
    while True:
        if P[p] == i:
            ret[i] = c
            break
        else:
            p = P[p]
            c += 1

val = [[0]*(N+1) for _ in range(N)]
for i in range(N):
    p = i
    temp = 0
    for j in range(1,N+1):
        p = P[p]
        temp += C[p]
        val[i][j] = temp


ans = -float('inf')
for i in range(N):
    if val[i][ret[i]] <= 0:
        temp_max = max(val[i][1:min(N,K)+1])
    else:
        temp1 = val[i][ret[i]]*(K//ret[i]) + max(val[i][:K-ret[i]*(K//ret[i])+1])
        temp2 = -float('inf')
        if K//ret[i] >= 1:
            temp2 = val[i][ret[i]]*(K//ret[i]-1) + max(val[i][:ret[i]+1])
        temp_max = max(temp1,temp2)
    ans = max(ans,temp_max)

print(ans)