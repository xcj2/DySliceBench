def binary_search_int(ok, ng, test, k, A, B):
    """
    :param ok: solve(x) = True を必ず満たす点
    :param ng: solve(x) = False を必ず満たす点
    """
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if test(mid, k, A, B):
            ok = mid
        else:
            ng = mid
    return ok

def get_cnt(x, A, B):
    """ a+b>=x となるようなAの要素とBの要素の組の数 (A, Bはソート済み)"""
    l, r = bisect_left(B, x-A[-1]), len(A)-2
    cnt = len(B) - l
    while l < len(B) and r>=0:
        if A[r]+B[l] < x:
            l += 1
        else:
            cnt += len(B) - l
            r -= 1
    return cnt

def test(x, k, A, B):
    return get_cnt(x, A, B) >= k

from bisect import *

X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()

P = []
for k in range(1,K+1):
    tmp = binary_search_int(0, 10**11,test, k, A, B)
    if tmp != 0:
        P.append(tmp)
Q = []
P.sort()
for k in range(1,K+1):
    Q.append(binary_search_int(1, 10**11,test, k, P, C))
print(*Q, sep="\n")
