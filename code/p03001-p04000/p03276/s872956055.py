#!/usr/bin/env python3
import sys


def append_zero(x):
    if 0 in x:
        return
    if x[0] > 0:
        x.insert(0, 0)
        return
    if x[len(x)-1] < 0:
        x.append(0)
        return
    for i in range(1, len(x)):
        if x[i-1] < 0 and x[i] > 0:
            x.insert(i, 0)
            return


def solve(N, K, x):
    y = [0]
    append_zero(x)
    n = len(x)
    z = 0
    for i in range(1, n):
        y.append(y[i-1] + x[i] - x[i-1])
        if x[i] == 0:
            z = i
    # print(x)
    # print(y)
    if n == K:
        if n-1 == z or z == 0:
            return y[n-1]
        else:
            l = y[z] + y[n-1]
            r = y[n-1] - y[z] + y[n-1]
            return min(l, r)
    ans = 10e20
    for i in range(n - K):
        k = i + K
        if k <= z:
            ans = min(ans, y[z] - y[i])
        if z <= i:
            ans = min(ans, y[k] - y[z])
        if i <= z and z < k:
            l = y[z] - y[i] + y[k] - y[i]
            r = y[k] - y[z] + y[k] - y[i]
            ans = min(ans, l, r)
    return ans


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(solve(N, K, x))


if __name__ == '__main__':
    main()
