#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int):
    c = 0
    i = 1
    ans = []
    while c <= N:
        c += i
        ans.append(i)
        i += 1
    
    t = c-N

    if c == N:
        print(ans)

    else:
        for i in ans:
            if i != t:
                print(i)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
