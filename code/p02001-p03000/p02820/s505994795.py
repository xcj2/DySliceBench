#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, K: int, R: int, S: int, P: int, T: str):
    s = ['b']*(N)
    
    l = [
        ['s', S],
        ['r', R],
        ['p', P]
    ]
    l = sorted(l, key=lambda x:-x[1])

    d = {
        'r':'p',
        's':'r',
        'p':'s'
    }

    for i in range(N):
        s[i] = d[T[i]]


    for a, b in l:
        for i in range(N):
            if s[i] == a and i >= K and s[i-K] == a:
                s[i] = 'b'

    ans = 0
    for i in range(N):
        if s[i] == 'r' and T[i] == 's':
            ans += R
        elif s[i] == 's' and T[i] == 'p':
            ans += S
        elif s[i] == 'p' and T[i] == 'r':
            ans += P
    print(ans)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    T = next(tokens)  # type: str
    solve(N, K, R, S, P, T)

if __name__ == '__main__':
    main()
