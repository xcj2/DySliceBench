import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)
mod = 10 ** 9 + 7


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

    def get(self, init=None):
        if self.v is None:
            return init
        else:
            return self.v


def main():
    N, MA, MB = read_values()
    dp = [
        [[10 ** 20 for b in range(N * 10 + 1)] for a in range(N * 10 + 1)]
        for n in range(N + 1)
    ]

    dp[0][0][0] = 0

    for n in range(1, N + 1):
        a, b, c = read_values()
        for aa in range(N * 10):
            for bb in range(N * 10 - b):
                if aa - a < 0 or bb - b < 0:
                    dp[n][aa][bb] = dp[n - 1][aa][bb]
                else:
                    dp[n][aa][bb] = min(
                        dp[n - 1][aa - a][bb - b] + c, dp[n - 1][aa][bb]
                    )

    res = V(min)
    max_k = (10 * N) // max(MA, MB)
    for k in range(1, max_k + 1):
        res.ud(dp[N][MA * k][MB * k])

    print(res if res.get() < 10 ** 20 else -1)


if __name__ == "__main__":
    main()
