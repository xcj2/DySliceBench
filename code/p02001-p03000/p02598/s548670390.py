import sys
import math

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def meguru_bisect(ok, ng):
        """
        is_okを定義して下さい
        :param ok: 取りうる最小の値-1
        :param ng: 取りうる最大の値+1
        :return: is_okを満たす最小(もしくは最大)の値
        """
        while abs(ok - ng) > 10 ** -5:
            mid = (ok + ng) / 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    def is_ok(x):
        cnt = 0
        for i in range(n):
            if A[i] > x:
                cnt += (A[i] + x - 1) // x - 1

        return cnt <= k

    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    res = meguru_bisect(10 ** 9 + 1, 0)
    print(math.ceil(res))


if __name__ == '__main__':
    resolve()
