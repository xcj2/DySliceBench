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

from itertools import product

H,W,K = LI()
S = [list(map(str, input())) for _ in range(H)]

A = product([0,1],repeat=H-1)
ans = float('inf')
for a in A:
    count = 0
    for a0 in a:
        if a0 == 1:
            count += 1
    List = []
    now = []
    for i in range(H):
        now.append(i)
        if i != H-1:
            if a[i] == 1:
                List.append(now)
                now = []
    List.append(now)
    n = len(List)
    nums = [0]*n
    now_nums = [0]*n
    for j in range(W):
        flag = False
        # L = [0,1]
        for k,L in enumerate(List):
            for l in L:
                if S[l][j] == '1':
                    now_nums[k] += 1
        #print(a,j,now_nums)         
        for k in range(n):
            if now_nums[k] > K:
                flag = True
                break
        
        c_flag = False
        for k in range(n):
            if nums[k]+now_nums[k] > K:
                count += 1
                c_flag = True
                break
        
        if c_flag:
            nums = now_nums[:]
            now_nums = [0]*n
        else:
            for k in range(n):
                nums[k] += now_nums[k]
            now_nums = [0]*n

        if flag:
            break
    if flag:
        continue

    if count < ans:
        ans = count

print(ans)