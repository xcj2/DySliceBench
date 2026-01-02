# -*- coding: utf-8 -*-
"""
https://beta.atcoder.jp/contests/abc084/tasks/abc084_d
AC
"""
import sys
from sys import stdin
from math import ceil, floor
input = stdin.readline


def create_prime_list(limit):
    """ エラトステネスの篩でlimitまでの素数リストを求める
    https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%A9%E3%83%88%E3%82%B9%E3%83%86%E3%83%8D%E3%82%B9%E3%81%AE%E7%AF%A9
    """
    x = limit**0.5
    primes = []
    #print('x={0}'.format(x))
    nums = [x for x in range(2, limit+1)]
    while nums[0]<=x:
        primes.append(nums[0])
        current_prime = nums[0]
        nums = [x for x in nums if x%current_prime != 0]
    primes.extend(nums)
    return primes


def solve(queries):
    primes = set(create_prime_list(10**5)) #  素数のテーブル、inでの判定が速くできるようにリストではなくセットにしておく
    dp = [0] * 100000

    # 1〜99,999までについて、1からのトータルで2017-likeな数字が累計でいくつあるか計算してテーブルにする
    p_num = 0
    for i in range(1, 100000, 2):
        if i in primes and ((i+1)//2) in primes:
            p_num += 1
        dp[i] = p_num

    # l 〜 r までで 2017-like数がいくつあるか求める
    for l, r in queries:
        if l == 1:
            ans = dp[r]         #  1からの場合、rまでの数がそのまま答え
        else:
            ans = dp[r] - dp[l-2] #  1〜rまでの数から 1〜l(エル)までの数を引けば、l〜rでの答えになる
        print(ans)


def main(args):
    queries = []
    Q = int(input())
    # Q = 0
    # for _ in range(100000):
    #     queries.append((1, 99999))
    queries = [map(int,input().split()) for _ in range(Q)]
    solve(queries)


if __name__ == '__main__':
    main(sys.argv[1:])
