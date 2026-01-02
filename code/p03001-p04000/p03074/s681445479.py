import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
sys.setrecursionlimit(10**7)
inf = 10 ** 20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def _I(): return int(sys.stdin.readline())
def _F(): return float(sys.stdin.readline())
def pf(s): return print(s, flush=True)

N, K = LI()
S = input()

positions = []
idx = 0
keep = None
while idx < N:
    if S[idx] == '0':
        if keep == None:
            keep = idx
    else:
        # 1の場合は無視
        if keep != None:
            positions.append([keep, idx])
            keep = None
        else:
            # keepしない場合
            keep = None
    idx += 1
else:
    if keep != None:
        positions.append([keep, keep+1])
#  print(positions)
if len(positions) == 0:
    print(N)
    exit()
elif len(positions) <= K:
    print(N)
    exit()

ans = 0

for idx in range(len(positions)):
    if idx + K - 1 > len(positions) - 1:
        break
    if idx == 0:
        left = 0
    else:
        left = positions[idx-1][1]

    if idx + K - 1 == len(positions)-1:
        end = N
    else:
        end = positions[idx+K-1+1][0]
    #  print(end, left)
    ans = max(ans, end - left)
print(ans)




    
