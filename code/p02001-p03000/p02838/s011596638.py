#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32

MOD = 1000000007  # type: int

def solve(N: int, A: "List[int]"):
    ans = [0] * 60
    
    
    for i in range(60):
        # x0 = len([j for j in range(N) if not (A[j]>>i)&1])
        # x1 = len([j for j in range(N) if (A[j]>>i)&1])
        x0 = 0
        x1 = 0
        for j in range(N):
            if (A[j]>>i)&1:
                x1 += 1
            else:
                x0 += 1

        ans[i] = x0*x1

    x = 0
    for i in range(len(ans)):
        # print(i, 2**i)
        x += pow(2, i) * ans[i] % MOD

    print(x%MOD)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
