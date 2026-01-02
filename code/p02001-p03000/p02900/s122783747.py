import sys
from math import ceil, sqrt


def input(): return sys.stdin.readline().strip()


def prime_factors(x):
    f = []
    for i in range(2, ceil(sqrt(x))+1):
        if x % i != 0:
            continue
        f.append([i, 0])
        while x % i == 0:
            x //= i
            f[-1][1] += 1
    if x != 1:
        f.append([x, 1])
    return f


def solve(A, B):
    d_a = set([x[0] for x in prime_factors(A)])
    d_b = set([x[0] for x in prime_factors(B)])
    return d_a & d_b


def main():
    A, B = map(int, input().split())
    ans = len(solve(A, B)) + 1
    print(ans)


if __name__ == "__main__":
    main()
