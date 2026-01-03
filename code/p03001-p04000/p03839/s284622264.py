#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)
INF = 1<<48


def solve(N: int, K: int, a: "List[int]"):

    v = [0] * (N+1)
    for i in range(N):
        v[i+1] = v[i]+a[i]
    w = [0] * (N+1)
    for i in range(N):
        w[i+1] = w[i] + max(0, a[i])

    ans = -INF
    for i in range(0, N-K+1):
        tmp = w[N]
        tmp += max(v[i+K]-v[i], 0)
        tmp -= w[i+K]-w[i]
        
        ans = max(ans, tmp)

    
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
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, a)

if __name__ == '__main__':
    main()
