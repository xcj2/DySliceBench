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
    use = [1 for i in range(N+1)]
    for i in range(N, 0, -1):
        multiple = sum([use[i] for i in range(i+i, N+1, i)])
        if A[i-1] == (1 + multiple) % 2:
            use[i] = 1
        else:
            use[i] = 0
    ans = [i for i in range(1, N+1) if use[i]]
    print(len(ans))
    if len(ans) > 0:
        print(*ans)


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
