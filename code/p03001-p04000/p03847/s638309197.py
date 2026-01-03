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
    N = format(int(input()), "b")
    D = len(str(N))
    dp = [[0 for _ in range(3)] for __ in range(D + 1)]

    dp[0][0] = 1
    for d in range(D):
        for k in range(3):
            for s in range(3):
                sd = 2 * s + int(N[d]) - k
                if sd > 2:
                    sd = 2
                if sd < 0:
                    continue
                dp[d + 1][sd] += dp[d][s]
                dp[d + 1][sd] %= mod

    print(sum(dp[D]) % mod)


if __name__ == "__main__":
    main()
