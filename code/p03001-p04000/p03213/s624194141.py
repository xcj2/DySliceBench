# -*- coding: utf-8 -*-
"""
D - 756
https://atcoder.jp/contests/abc114/tasks/abc114_d

"""
import sys


from collections import Counter

def prime_factor(N):
    factors = Counter()
    for i in range(2, int(N**0.5)+1):
        while N % i == 0:
            factors[i] += 1
            N //= i
    if N != 1:
        factors[N] = 1
    return factors


def solve(n):
    d = Counter()
    for i in range(2, n+1):
        x = prime_factor(i)
        d += x
    t3 = [v for k, v in d.items() if v >= 2]
    t5 = [v for k, v in d.items() if v >= 4]
    t15 = [v for k, v in d.items() if v >= 14]
    t25 = [v for k, v in d.items() if v >= 24]
    t75 = [v for k, v in d.items() if v >= 74]
    ans = len(t75) + len(t25)*(len(t3)-1) + len(t15)*(len(t5)-1)+len(t5)*(len(t5)-1)*(len(t3)-2) // 2
    return ans


def main(args):
    n = int(input())
    ans = solve(n)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
