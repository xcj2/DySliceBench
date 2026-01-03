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
    N = int(input())
    A = [(int(input()), n % 2) for n in range(N)]
    A.sort()

    res = 0
    for i, (_, j) in enumerate(A):
        if i % 2 != j:
            res += 1

    print(res // 2)


if __name__ == "__main__":
    main()
