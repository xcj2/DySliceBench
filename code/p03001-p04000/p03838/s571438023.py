#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)
INF = 1<<32


def solve(x: int, y: int):
    ans = 0
    
    if x == y:
        ans = 0
    elif abs(x) == abs(y):
        ans = 1
    elif x < y <= 0:
        ans = abs(y-x)
    elif 0 <= x < y:
        ans = abs(y-x) 
    elif x < 0 <= y:
        ans = min(y-x, abs(abs(x)-abs(y))+1)
    elif y < x <= 0:
        if x == 0:
            ans = -y+1
        else:
            ans = 1-y+x+1
    elif 0 <= y < x:
        if y == 0:
            ans = x+1
        else:
            ans = 2+x-y
    elif y < 0 <= x:
        if x == 0:
            ans = -y-x+1
        else:
            ans = abs(abs(x)-abs(y))+1

    print(ans)
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    x = int(next(tokens))  # type: int
    y = int(next(tokens))  # type: int
    solve(x, y)

if __name__ == '__main__':
    main()
