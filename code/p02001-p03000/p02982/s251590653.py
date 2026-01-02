#!/usr/bin/env python3
import sys
import math
def isSquare(x):
    x_sqrt = int(math.floor(math.sqrt(x)))
    if x_sqrt * x_sqrt == x:
        return True
    else:
        return False

def distSquare(a, b, D):
    result = 0
    for i in range(D):
        result += (a[i]-b[i]) * (a[i]-b[i])
    return result

def solve(N: int, D: int, X: "List[List[int]]"):
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if isSquare(distSquare(X[i], X[j], D)):
                count += 1
    print(count)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    X = [ [ int(next(tokens)) for _ in range(D) ] for _ in range(N) ]  # type: "List[List[int]]"
    solve(N, D, X)

if __name__ == '__main__':
    main()
