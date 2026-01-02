import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def meguru_bisect(left, right):
        """
        is_okを定義して下さい
        :param left: 取りうる最小の値-1
        :param right: 取りうる最大の値+1
        :return: is_okを満たす最小(もしくは最大)の値
        """
        while abs(left - right) > 1:
            mid = (left + right) // 2
            if is_ok(mid):
                right = mid
            else:
                left = mid
        return right

    def is_ok(x):
        total = 0
        for i in range(n):
            total += max(0, A[i] - x // F[i])
        return total <= k

    n, k = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    F = sorted(list(map(int, input().split())), reverse=True)

    left = -1
    right = 10 ** 12 + 1
    res = meguru_bisect(left, right)
    print(res)


if __name__ == '__main__':
    resolve()
