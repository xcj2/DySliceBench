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

N, K = mi()
S = input()
inds = [[0, 0]]

flag = 0
s = 0
for i in range(N):
    if S[i] == '0':
        if not flag:
            flag = 1
            inds.append([s, i-1])
    else:
        if flag:
            s = i
        flag = 0
if flag:
    inds.append([N-1, N-1])
if not flag:
    inds.append([s, N-1])
#print(inds)
l_inds = len(inds)
wa = 0
if K >= l_inds-1:
    print(N)
    exit()
for i in range(l_inds-K):
    wa = max(inds[i+K][1] - inds[i][0] + 1, wa)

print(wa)