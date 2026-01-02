import sys
from bisect import bisect_right

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def is_ok_m(x):
        cnt = 0
        for P in plus:
            t = x // P
            cnt += bisect_right(minus, t)
        return cnt >= k

    def is_ok_p(x):
        cnt = 0
        for i, P in enumerate(plus):
            t = x // P
            idx = bisect_right(plus, t)
            if i < idx:
                idx -= 1
            cnt += idx

        for i, M in enumerate(minus):
            t = x // M
            idx = bisect_right(minus, t)
            if i < idx:
                idx -= 1
            cnt += idx
        cnt //= 2
        return cnt >= k

    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    minus, plus = [], []
    z = 0
    for a in A:
        if a < 0:
            minus.append(a)
        elif a > 0:
            plus.append(a)
        else:
            z += 1
    m, p = len(minus), len(plus)

    m_cnt = m * p
    z_cnt = m * z + p * z + ((z - 1) * z) // 2
    if k <= m_cnt:
        minus.sort()
        ng, ok = -10 ** 18 - 1, -1
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if is_ok_m(mid):
                ok = mid
            else:
                ng = mid
        res = ok
    elif k <= m_cnt + z_cnt:
        res = 0
    else:
        k -= m_cnt + z_cnt
        plus.sort()
        minus = [num * -1 for num in minus]
        minus.sort()
        ng, ok = -1, 10 ** 18
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if is_ok_p(mid):
                ok = mid
            else:
                ng = mid
        res = ok
    print(res)


if __name__ == '__main__':
    resolve()
