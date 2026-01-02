import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
from math import gcd
from functools import reduce

def gcd_list(numbers):
    return reduce(gcd, numbers)

K = ii()
ans = 0

memo = dp3(-1, K+1, K+1, K+1)

for i in range(1, K+1):
    for j in range(1, K+1):
        for k in range(1, K+1):
            #l = sorted([i, j, k])
            #l = [i, j, k]
            #a, b, c = l[0], l[1], l[2]
            a, b, c = i, j, k
            if memo[a][b][c] != -1:
                ans += memo[a][b][c]
            else:
                memo[a][b][c] = gcd_list([a, b, c])
                memo[i][k][j] = memo[k][i][j] = memo[k][j][i] = memo[j][i][k] = memo[j][k][i] = memo[i][j][k]
                #memo[i][k][j] = memo[i][j][k]
                #memo[k][i][j] = memo[i][j][k]
                #memo[k][j][i] = memo[i][j][k]
                #memo[j][j][i] = memo[i][j][k]
                #memo[j][i][k] = memo[i][j][k]
                ans += memo[a][b][c]
            #ans += gcd_list([i, j, k])


print(ans)