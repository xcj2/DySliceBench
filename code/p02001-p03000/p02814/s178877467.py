import sys
import functools
from math import gcd


def lcm2(x, y):
    return x * y // gcd(x, y)


def lcm(x):
    return functools.reduce(lcm2, x)


def resolve(in_):
    N, M = map(int, next(in_).split())
    A = tuple(map(lambda x: int(x) // 2, next(in_).split()))

    a0 = A[0]
    x = 0
    while True:
        a0, b = divmod(a0, 2)
        if b:
            break
        x += 1
    x = 2 ** x
    for a in A[1:]:
        d, m = divmod(a, x)
        if m != 0 or not d % 2:
            return 0 

    l = lcm(A)
    l2 = l + l

    answer = len(range(l, M + 1, l2))

    return answer


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()
