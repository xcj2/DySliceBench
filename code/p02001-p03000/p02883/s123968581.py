import sys
input = sys.stdin.readline

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


N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
F = list(map(int, input().split()))
F.sort(reverse=True)

def max2(x,y):
    return x if x > y else y

def test(x):
    temp = K
    for a, f in zip(A, F):
        temp -= max2((a - x//f), 0)
        if temp < 0:
            return False
    return True

print(binary_search_int(A[-1]**2 + 100, -1,test))
