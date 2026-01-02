#!/usr/bin/env python3
import sys
MOD = 2  # type: int

def solve(S, k, p, M, N):
    count = 0
    for sw in range(2**N):
        sw_str = bin(sw)[2:].zfill(N)
        sw_list = list(map(int, list(sw_str)))
        isGood = True
        for i in range(M):
            bsum = 0
            for j in range(k[i]):
                bsum += sw_list[S[i][j]]
            if bsum % 2 != p[i]:
                isGood = False
                break
        if isGood:
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
    M = int(next(tokens))  # type: int
    k = [0] * M
    p = [0] * M
    S = []
    for i in range(M):
        k[i] = int(next(tokens))
        S += [ [int(next(tokens))-1 for j in range(k[i]) ] ]
    for i in range(M):
        p[i] = int(next(tokens))

    solve(S, k, p, M, N)

if __name__ == '__main__':
    main()
