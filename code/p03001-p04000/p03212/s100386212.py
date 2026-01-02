import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
import itertools #list(accumulate(A))
from collections import deque

N = ii()
ele = [3, 5, 7]
l = []

def dfs(num, flag3, flag5, flag7):
    #print(num, flag3, flag5, flag7)
    if num > N:
        return 
    if flag3 is flag5 is flag7 is True:
        l.append(num)
    num *= 10
    dfs(num+3, True, flag5, flag7)
    dfs(num+5, flag3, True, flag7)
    dfs(num+7, flag3, flag5, True)

dfs(0, False, False, False)
print(len(l))
