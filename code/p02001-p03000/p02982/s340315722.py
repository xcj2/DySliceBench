#!/usr/bin/env python3


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h() if m > 1 else typ(input()) for _ in range(n)]


def main():
    N, D = read_h()
    X = read_v(N, m=D)

    import numpy as np

    cnt = 0
    for i in range(0, N - 1):
        for j in range(i + 1, N):
            dist = np.sqrt(np.sum(np.power(np.asarray(X[i]) - np.asarray(X[j]), 2)))
            if dist - np.floor(dist) == 0.0:
                cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
