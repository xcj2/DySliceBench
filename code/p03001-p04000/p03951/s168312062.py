#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, s: str, t: str):
    
    ans = 0
    for i in range(N):
        m = 0
        for j in range(N):
            if i+j < N and s[i+j] == t[j]:
                m += 1
            else:
                break
        ans = max(ans, m)

    print(2*N-ans)   

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    s = next(tokens)  # type: str
    t = next(tokens)  # type: str
    solve(N, s, t)

if __name__ == '__main__':
    main()
