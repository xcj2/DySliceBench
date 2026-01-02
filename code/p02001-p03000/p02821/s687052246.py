"""
チルノ（無色）のプログラミング教室～☆

こんなの無色コーダーのレベルじゃないよ～
え？　ABC D-Pairs とほとんど同じ方針？
こんな典型問題も解けないから灰色にすらなれない無色なんだよ、だって？
うわーん、無色っていうなー！！！
"""


def get_count(x):
    """
    :return: x 以上となる組の数
    """
    cnt = 0
    for i in range(N):
        cnt += bisect_left(A, x-A[i])
    res = N**2 - cnt
    return res

def binary_search_int(ok, ng, test):
    """
    :param ok: solve(x) = True を必ず満たす点
    :param ng: solve(x) = False を必ず満たす点
    """
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if test(mid):
            ok = mid
        else:
            ng = mid
    return ok

def test(x):
    return get_count(x) >= M

def get_sum(x):
    res = 0
    cnt = 0
    for i in range(N):
        temp = bisect_left(A, x-A[i])
        res += A[i]*(N - temp) + B[-1] - B[temp]
        cnt += N - temp
    return res - x*(cnt-M)

################################################################

from bisect import *
from itertools import accumulate

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
B = list(accumulate([0] + A))

print(get_sum(binary_search_int(0, 2*10**5+10, test)))