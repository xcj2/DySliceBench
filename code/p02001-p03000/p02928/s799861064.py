#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)

MOD = 1000000007  # type: int

def solve(N: int, K: int, A: "List[int]"):
    ret = 0
    for i in range(N):
        for j in range(i + 1, N):
            tmp = 0
            if A[i] > A[j]:
                tmp = K * (K + 1) // 2
            elif A[i] < A[j]:
                tmp = (K - 1) * K // 2
            ret += tmp
            ret %= MOD
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [ int(next(tokens)) for _ in range(N-1-0+1) ]  # type: "List[int]"
    solve(N, K, A)

if __name__ == '__main__':
    main()
