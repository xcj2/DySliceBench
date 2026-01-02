# -*- coding: utf-8 -*-
"""
D - Partition
https://atcoder.jp/contests/abc112/tasks/abc112_d

"""
import sys


from bisect import bisect_right

def solve(N, M):
    def divisor(N):
        divisors = set()
        for i in range(1, int(N**0.5)+1):
            if N % i == 0:
                divisors.add(i)
                divisors.add(N // i)
        return divisors

    div_M = sorted(list(divisor(M)))
    i = bisect_right(div_M, M/N)
    if i:
        return div_M[i-1]
    else:
        return 1



def main(args):
    N, M = map(int, input().split())
    ans = solve(N, M)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
