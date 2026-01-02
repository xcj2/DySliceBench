#!/usr/bin/env python3
import sys


def solve(N: int, K: int, V: "List[int]"):
    l = [0] * (K + 1)
    r = [0] * (K + 1)
    for i in range(1, K + 1):
        v = V[:i]
        v.sort(reverse=True)
        for j in range(0, i):
            if i + j <= K:
                l[i + j] = max(l[i + j], sum(v[:i - j]))

    V.reverse()
    for i in range(1, K + 1):
        v = V[:i]
        v.sort(reverse=True)
        for j in range(0, i):
            if i + j <= K:
                r[i + j] = max(r[i + j], sum(v[:i - j]))

    for i in range(1, K + 1):
        l[i] = max(l[i], l[i - 1])
        r[i] = max(r[i], r[i - 1])

    #print(l)
    #print(r)
    ret = 0
    for i in range(0, len(l)):
        ret = max(ret, l[i] + r[K - i])
        #print(l[i], r[K - i], ret)

    tmp = 0
    for v in V:
        if v > 0:
            tmp += v
    ret = min(ret, tmp)
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    V = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, K, V)

if __name__ == '__main__':
    main()
