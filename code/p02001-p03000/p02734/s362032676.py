import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)
# mod = 10 ** 9 + 7
mod = 998244353


def read_values():
    return map(int, input().split())


def read_index():
    return map(lambda x: int(x) - 1, input().split())


def read_list():
    return list(read_values())


def read_lists(N):
    return [read_list() for n in range(N)]


class V:
    def __init__(self, f, v=None):
        self.f = f
        self.v = v

    def __str__(self):
        return str(self.v)

    def ud(self, n):
        if n is None:
            return

        if self.v is None:
            self.v = n
            return
        self.v = self.f(self.v, n)


def main():
    N, S = read_values()
    A = read_list()

    dp = [(0, 0, 0) for _ in range(S + 1)]
    dp[0] = (1, 1, 1)

    for a in A:
        for s in range(S, -1, -1):
            d1 = dp[s][0]
            d2 = (dp[s][1] + (0 if s - a < 0 else dp[s - a][1]) + d1) % mod
            d3 = (dp[s][2] + (0 if s - a < 0 else dp[s - a][1]) + d2) % mod
            dp[s] = (d1, d2, d3)

    print((dp[S][2] - dp[S][1]) % mod)


if __name__ == "__main__":
    main()
