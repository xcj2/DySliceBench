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

S = str(input())
T = str(input())

ans = float('inf')
for i in range(len(S)):
    count = 0
    flag = False
    for j in range(len(T)):
        if i+j >= len(S):
            flag = True
            break
        if S[i+j] != T[j]:
            count += 1
    if flag:
        continue
    else:
        ans = min(ans,count)

print(ans)