#!/usr/bin/env python3
import sys
import math

def solve(N: int, a: "List[int]"):
    # 素因数分解して，2の個数 == ans
    def factorization(n):
        factor = []
        n_ = n
        for i in range(2, int(math.sqrt(n) + 1)):
            if i == 3:
                break
            if n_ % i == 0:
                cnt = 0
                while n_ % i == 0:
                    n_ = n_ // i
                    cnt += 1
                factor.append([i, cnt])
        if n_ != 1:
            factor.append([n_, 1])
        if n == []:
            factor.append([n, 1])
        return factor

    ans = 0
    for ai in a:
        factor = factorization(ai)
        if factor[0][0] == 2:
            ans += factor[0][1]

    print(ans)

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
