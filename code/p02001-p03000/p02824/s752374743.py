import sys
from copy import deepcopy

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def meguru_bisect(ok, ng):
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    def is_ok(x):
        B = deepcopy(A)
        total = m * v
        target = B[x] + m
        for i in range(n):
            if i <= x:
                B[i] += m
                total -= m
            else:
                if n - (p - 1) <= i:
                    B[i] += m
                    total -= m
                else:
                    if B[i] > target:
                        return False
                    else:
                        total -= target - B[i]
                        B[i] = target
        return total <= 0

    n, m, v, p = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    ng, ok = n, -1
    res = meguru_bisect(ng, ok)
    print(n - res)


if __name__ == '__main__':
    resolve()
