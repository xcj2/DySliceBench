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

N = ii()
xyh = li2(N)

for c_x in range(101):
    for c_y in range(101):
        flag = 0
        left = 1
        right = float('inf')
        for i in range(N):
            #print(i, left, right)
            tmp = xyh[i][2] + abs(c_x-xyh[i][0]) + abs(c_y-xyh[i][1])
            #print(tmp, xyh[i][2])
            if xyh[i][2] > 0:
                if not(left <= tmp <= right):
                    flag = 1
                    break
                left = right = tmp
            else:
                if tmp < 1 or left > tmp:
                    flag = 1
                    break
                right = min(right, tmp)
        if not flag:
            print(c_x, c_y, right)
            exit()