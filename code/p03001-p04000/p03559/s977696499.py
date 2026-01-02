#!/usr/bin/env python3
import sys

def fill(D, A, c):
    for a in A:
        if a not in D:
            D[a] = {'A': 0, 'B': 0, 'C': 0}
        D[a][c] += 1


def solve(N: int, A, B, C):
    D = {}
    fill(D, A, 'A')
    fill(D, B, 'B')
    fill(D, C, 'C')
    D = sorted(D.items(), key=lambda x: x[0], reverse=True)

    a = 0
    b = 0
    c = 0
    for k, v in D:
        a += b * v['A']
        b += c * v['B']
        c += v['C']

    print(a)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    A = [int(next(tokens)) for _ in range(N)]
    B = [int(next(tokens)) for _ in range(N)]
    C = [int(next(tokens)) for _ in range(N)]
    solve(N, A, B, C)

if __name__ == '__main__':
    main()
