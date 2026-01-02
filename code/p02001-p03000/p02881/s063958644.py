#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)
INF = 1<<48


def solve(N: int):
    # 約数の全列挙
    def divisors(n):
        divisors = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n//i)
        # divisors.sort(reverse=True)  # ソート
        return divisors

    l = divisors(N)
    l.append(1)
    l.sort()

    ans = INF

    for i in l:
        M = N // i
        ans = min(ans, M+i-2)

    print(ans)

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
