#!/usr/bin/env python3
import sys


def solve(N: int, x: "List[float]", u: "List[str]"):
    ret = 0
    for i in range(N):
        if u[i] == "JPY":
            ret += x[i]
        else:
            ret += 380000.0 * x[i]
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = [float()] * (N)  # type: "List[float]" 
    u = [str()] * (N)  # type: "List[str]" 
    for i in range(N):
        x[i] = float(next(tokens))
        u[i] = next(tokens)
    solve(N, x, u)

if __name__ == '__main__':
    main()
