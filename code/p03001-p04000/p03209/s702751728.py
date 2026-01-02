def PAndB(n):
    return (2 ** (n + 2)) - 3


def allPatty(n):
    return (2 ** (n + 1)) - 1


def count(N, X):
    if N == 0:
        return 1
    elif X <= N:
        return 0
    elif X >= PAndB(N) - (N - 1):
        return allPatty(N)
    elif X == PAndB(N - 1) + 2:
        return allPatty(N - 1) + 1
    elif X <= PAndB(N - 1) + 1:
        return count(N - 1, X - 1)
    else:
        return allPatty(N - 1) + 1 + count(N - 1, X - (PAndB(N - 1) + 2))


def main():
    N, X = map(int, input().split())
    print(count(N, X))


if __name__ == '__main__':
    main()