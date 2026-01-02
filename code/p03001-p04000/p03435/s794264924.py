#!/usr/bin/env python3


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h() if m > 1 else typ(input()) for _ in range(n)]


def main():
    c = read_v(n=3, m=3)

    # Assume a_1 = 0 without loss of generality
    a = [0, 0, 0]
    b = c[0]
    for i in (1, 2):
        a[i] = c[i][0] - b[0]

    # Check if Takahashi is correct
    for i in range(3):
        for j in range(3):
            if c[i][j] != a[i] + b[j]:
                print('No')
                return

    print('Yes')


if __name__ == '__main__':
    main()
