#!/usr/bin/env python3
import sys

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def solve(N: int, A: "List[int]"):
    tmp = A[0]
    l = []
    for a in A:
        tmp = gcd(tmp, a)
        l.append(tmp)
    tmp = A[-1]
    r = []
    for a in A[::-1]:
        tmp = gcd(tmp, a)
        r.append(tmp)
    r.reverse()
    ret = 0
    for i in range(N):
        if i < 1:
            tmp = r[i + 1]
        elif i >= N - 1:
            tmp = l[i - 1]
        else:
            tmp = gcd(l[i - 1], r[i + 1])
        ret = max(ret, tmp)
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
