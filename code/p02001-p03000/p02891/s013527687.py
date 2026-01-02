import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from itertools import accumulate #list(accumulate(A))

S = input()
N = len(S)
K = ii()
cnt = 0
#for i in range(1, N):
i = 1
flag = 0

if S.count(S[0]) == N:
    print(N * K // 2)
    exit()

while i < N:
    if S[i] == S[i-1]:
        cnt += 1
        if i + 1 < N and S[i] == S[i+1]:
            i += 1
        if i == N-1:
            flag = 1
    i += 1

if flag and S[0] == S[-1]:
    cnt += 1
    cnt_sub = 0
    S = S[1:] + S[0]
    i = 1
    flag = 0
    while i < N:
        if S[i] == S[i-1]:
            cnt_sub += 1
            if i + 1 < N and S[i] == S[i+1]:
                i += 1
        i += 1
    print(cnt + cnt_sub * (K-2) + cnt_sub - 1)

else:
    print(cnt * K)