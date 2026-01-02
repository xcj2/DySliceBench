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
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def pf(s): return print(s, flush=True)

N, Q = LI()
s = input()
TD = []
T, D = [], []
for i in range(Q):
    t,d = LS()
    TD.append([t,d])

def get_mid(lb, ub):
    if lb + ub < 0:
        return 0
    else:
        return (lb + ub) // 2
# 左から落ちるものの探索
# 2回midが同じならやめる
def find_left_dropped():
    lb, ub = -1, N
    while True:
        if lb + ub < 0:
            mid = 0
        else:
            mid = (lb + ub) // 2
        original_mid = mid
        for td in TD:
            if td[0] == s[mid]:
                if td[1] == "L":
                    mid -= 1
                else:
                    mid += 1

                if mid == -1:
                    # 左に落ちた
                    lb = original_mid
                    if get_mid(lb, ub) == original_mid:
                        return original_mid+1
                    break
                
                if mid == N:
                    # 右に落ちた
                    ub = original_mid
                    if get_mid(lb, ub) == original_mid:
                        return original_mid
                    break
        else:
            # 落ちなかった
            ub = original_mid
            if get_mid(lb, ub) == original_mid:
                return original_mid

def find_right_dropped():
    lb, ub = -1, N
    while True:
        if lb + ub < 0:
            mid = 0
        else:
            mid = (lb + ub) // 2
        original_mid = mid
        for td in TD:
            if td[0] != s[mid]:
                continue

            if td[1] == "L":
                mid -= 1
            else:
                mid += 1

            if mid == -1:
                # 左に落ちた
                lb = original_mid
                if get_mid(lb, ub) == original_mid:
                    return original_mid+1
            
            if mid == N:
                # 右に落ちた
                ub = original_mid
                if get_mid(lb, ub) == original_mid:
                    return original_mid
                break
        else:
            # 落ちなかった
            lb = original_mid
            if get_mid(lb, ub) == original_mid:
                return original_mid + 1

left_survived = find_left_dropped()
#  print(left_survived)
right_survived = find_right_dropped()
#  print(right_survived)

result = right_survived - left_survived
print(result)
