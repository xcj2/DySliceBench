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
#import itertools #list(accumulate(A))
#from collections import deque

## FlagをもたせたDFS

N = ii()
ele = [3, 5, 7]
l = []

def dfs(num, flag):
    if num > N:
        return 
    if flag == 7:
        l.append(num)
    num *= 10
    for i, e in enumerate(ele):
        dfs(num+e, flag | 1<<i)

dfs(0, 0)
print(len(l))