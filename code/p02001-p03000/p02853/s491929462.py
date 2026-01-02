#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(X: int, Y: int):
    ans = 0
    if X == 3:
        ans += 1
    elif X == 2:
        ans += 2
    elif X == 1:
        ans += 3
    
    if Y == 3:
        ans += 1
    elif Y == 2:
        ans += 2
    elif Y == 1:
        ans += 3
    
    if X == 1 and Y == 1:
        ans += 4
    
    print(ans*10**5)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    solve(X, Y)

if __name__ == '__main__':
    main()
