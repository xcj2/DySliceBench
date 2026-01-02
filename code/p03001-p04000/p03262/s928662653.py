#!/usr/bin/env python3
import sys

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solve(N: int, X: int, x: "List[int]"):
    dis = []
    for a in x:
        dis.append(abs(X - a))
    ret = dis[0]
    for i in range(1, len(dis)):
        ret = gcd(ret, dis[i])
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    x = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, X, x)

if __name__ == '__main__':
    main()
