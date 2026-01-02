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

from bisect import bisect_right

N,K = LI()
A = LI()

# 各値の場所
d = defaultdict(list)
for i in range(N):
    d[A[i]].append(i)

# 各場所スタートでの，終了時の先頭要素
T = [0]*(N+1)
for i in range(N)[::-1]:
    p = bisect_right(d[A[i]],i)
    if p < len(d[A[i]]):
        T[i] = T[d[A[i]][p]+1]
    else:
        T[i] = A[i]

# 各indexスタートが何週目の操作で起こるか
S = defaultdict(list)
index = 0
roop_flag = False
empty_flag = False
for i in range(1,N+2):
    S[index].append(i)
    if len(S[index]) > 1:
        start = S[index][0]
        end = S[index][1]
        roop_flag = True
        break
    n = T[index]
    if n == 0:
        num = i
        empty_flag = True
        break
    index = d[n][0]+1

def request_s(index):
    ret = []
    while index <= N-1:
        p = bisect_right(d[A[index]],index)
        if p < len(d[A[index]]):
            index = d[A[index]][p]+1
        else:
            ret.append(A[index])
            index += 1
    return ret

if roop_flag:
    if K <= start:
        index = 0
        for i in range(K-1):
            index = d[T[index]][0]+1
        ans = request_s(index)
    else:
        index = 0
        for i in range(start-1):
            index = d[T[index]][0]+1
        left = (K-(start-1)) % (end-start+1)
        if left == 0:
            left = end-start+1
        for i in range(left-1):
            index = d[T[index]][0]+1
        ans = request_s(index)
else:
    K = K%num
    index = 0
    if K == 0:
        ans = []
    else:
        for i in range(K-1):
            index = d[T[index]][0]+1
        ans = request_s(index)

print(*ans)