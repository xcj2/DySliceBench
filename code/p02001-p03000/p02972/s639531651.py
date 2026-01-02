import sys
input = sys.stdin.readline
from collections import defaultdict


def read():
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    return N, A


def divisor(n):
    i = 1
    d = []
    while i * i <= n:
        if n % i == 0:
            d.append(i)
            if i * i != n:
                d.append(n // i)
        i += 1
    return d


def solve(N, A):
    ans = []
    for i in range(N, 0, -1):
        if A[i-1] == 1:
            ans += [i]
            for d in divisor(i):
                A[d-1] ^= 1
    print(len(ans))
    print(*ans)


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
