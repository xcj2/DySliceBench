import sys
input = sys.stdin.readline
sys.setrecursionlimit(2 * 10**6)


def inpl():
    return list(map(int, input().split()))


def backtrack(n, ml, mh, tmp=[]):
    if n == 0:
        yield tmp
        return

    for i in range(ml, mh + 1):
        yield from backtrack(n - 1, i, mh, tmp + [i])


def main():
    def count(ca):
        return sum(d for a, b, c, d in abcd if ca[b - 1] - ca[a - 1] == c)
    N, M, Q = inpl()
    abcd = [inpl() for _ in range(Q)]
    print(max(count(c) for c in backtrack(N, 1, M)))


if __name__ == '__main__':
    main()
