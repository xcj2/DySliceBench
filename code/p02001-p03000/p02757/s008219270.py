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
    N, P = read_values()
    S = input().strip()

    if P in (2, 5):
        res = 0
        for i, s in enumerate(S):
            if int(s) % P == 0:
                res += i + 1
        print(res)

    else:
        r = 0
        D = {0: 1}
        res = 0
        d = 1
        for i, s in enumerate(S[::-1]):
            r += int(s) * d
            r %= P
            d *= 10
            d %= P
            c = D.setdefault(r, 0)
            res += c
            D[r] += 1
        print(res)


if __name__ == "__main__":
    main()
