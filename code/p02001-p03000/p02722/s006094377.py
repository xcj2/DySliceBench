#!/usr/bin/python3
# import bisect
# from collections import Counter, deque, OrderedDict, defaultdict
from copy import copy, deepcopy # pythonのみ．copyは1次元，deepcopyは多次元．
# from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
# from functools import reduce
# from heapq import heapify, heappop, heappush
# from itertools import accumulate, permutations, combinations, combinations_with_replacement, groupby, product
# import math
# import numpy as np  # Pythonのみ！
# from operator import xor
# import re
# from scipy.sparse.csgraph import connected_components  # Pythonのみ！
# ↑cf.  https://note.nkmk.me/python-scipy-connected-components/
# from scipy.sparse import csr_matrix
# import statistics # Pythonのみ
# import string
import unittest
from io import StringIO
import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():

    n = int(input())

    import math

    # cf. https://qiita.com/suecharo/items/14137fb74c26e2388f1f

    def make_prime_list_2(num):
        if num < 2:
            return []

        # 0のものは素数じゃないとする
        prime_list = [i for i in range(num + 1)]
        prime_list[1] = 0  # 1は素数ではない
        num_sqrt = math.sqrt(num)

        for prime in prime_list:
            if prime == 0:
                continue
            if prime > num_sqrt:
                break

            for non_prime in range(2 * prime, num, prime):
                prime_list[non_prime] = 0

        return [prime for prime in prime_list if prime != 0]

    def prime_factorization_2(num):
        """numの素因数分解
        素因数をkeyに乗数をvalueに格納した辞書型dict_counterを返す"""

        if num <= 1:
            return False
        else:
            num_sqrt = math.floor(math.sqrt(num))
            prime_list = make_prime_list_2(num_sqrt)

            dict_counter = {}  # 何度もこの関数を呼び出して辞書を更新したい時はこれを引数にして
            # cf. https://atcoder.jp/contests/arc034/submissions/12251452

            for prime in prime_list:
                while num % prime == 0:
                    if prime in dict_counter:
                        dict_counter[prime] += 1
                    else:
                        dict_counter[prime] = 1
                    num //= prime
            if num != 1:
                if num in dict_counter:
                    dict_counter[num] += 1
                else:
                    dict_counter[num] = 1

            return dict_counter

    def divisor_count(num):
        """numの約数の個数を求める"""
        if num < 0:
            return None
        elif num == 1:
            return 1
        else:
            divisor_num = 1
            dict_fact = prime_factorization_2(num)
            for value in dict_fact.values():
                divisor_num *= (value + 1)
            return divisor_num

    ans = divisor_count(n-1)

    def make_divisors(n):
        divisors = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:  # 平方数の場合n**0.5を1つだけにしてる
                    divisors.append(n//i)

        # divisors.sort() # ソートしたけりゃして
        return divisors

    l = make_divisors(n)

    def main():
        cnt = 0
        for i in l:
            if i==1: continue
            v = copy(n)
            while v % i == 0:
                v /= i
            v%=i
            if v==1: cnt += 1
        return cnt

    print(ans+main()-1)


resolve()