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

def edges_to_pt(s,t,n,directed=False):
    pt = [[] for _ in range(n)]
    for i in range(len(s)):
        pt[s[i]-1].append(t[i]-1)
        if not directed:
            pt[t[i]-1].append(s[i]-1)
    return pt

N,M = LI()
H = LI()
A,B = LIR(M,2)

pt = edges_to_pt(A,B,N)

ans = 0
used = [False]*N
for i in range(N):
    flag = True
    if not used[i]:
        for j in pt[i]:
            if H[j] > H[i]:
                used[i] = True
                flag = False
                break
            elif H[j] == H[i]:
                flag = False
                used[j] = True
            else:
                used[j] = True
    if used[i]:
        flag = False
    if flag:
        ans += 1
print(ans)