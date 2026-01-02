#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int


def solve(N: int, K: int):
    count = [0]*(K+1)

    answer = 0
    for k in range(K,0,-1): #kの倍数のもの
        d = K//k
        if k == 1:
            answer += pow(K,N,MOD)-sum(count) 
        else:
            count[k] = pow(d,N,MOD)
            i = 2
            while k*i <= K:
                count[k] -= count[k*i]
                i += 1
            answer += count[k]*k
        answer %= MOD
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, K)

if __name__ == '__main__':
    main()
