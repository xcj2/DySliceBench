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

def dfs(ind, l):
    if ind == 4:
        if sum(l) ==7:
            for i, num in enumerate(l):
                if num >= 0 and i != 0:
                    print('+', end='')
                print(num, end='')
        else:
            return
        print('=7')
        exit()
    dfs(ind+1, l+[A[ind]])
    dfs(ind+1, l+[(-1)*A[ind]])

A = list(map(int, list(input())))
dfs(1, [A[0]])