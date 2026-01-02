#揃える長さを決め打って二分探索
import sys
import math
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n,k = map(int,readline().split())
lst1 = list(map(int,readline().split()))
lst1.sort(reverse=True)
def func(mid): #ここが関数部分
    res = 0
    for i in range(n):
        if mid >= lst1[i]:
            continue
        res += math.ceil(lst1[i]/mid)-1
        if res > k:
            return False
    return True


def binary_search(): #2分探索
    ok = 10**9
    ng = 0
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if func(mid):
            ok = mid
        else:
            ng = mid

    return ok

print(binary_search())