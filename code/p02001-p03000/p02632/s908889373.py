# coding: utf-8
import sys
# from operator import itemgetter
sysread = sys.stdin.readline
read = sys.stdin.read
sys.setrecursionlimit(10 ** 7)
#from heapq import heappop, heappush
#from collections import OrderedDict, defaultdict
#import math
#from itertools import product, accumulate, combinations, product
#import bisect# lower_bound etc
#import numpy as np
#from copy import deepcopy
#from collections import deque
#import numba

def run():
    K = int(input())
    S = input()
    L = len(S)
    mod = 10 ** 9 +7
    def comb_mod2(n, a, mod):
        """
        return: [n, a] % mod
        Note: mod must be a prime number
        """
        if a == 0:
            return 1 % mod
        ret = 1
        for i in range(1, a + 1):
            ret *= n - i + 1
            ret %= mod
            ret *= inv[i]
            ret %= mod
        return ret

    ##################################################################
    def generate_inv(n, mod):
        """
        逆元行列
        n >= 2
        Note: mod must bwe a prime number
        """
        ret = [0, 1]
        for i in range(2, n + 1):
            next = -ret[mod % i] * (mod // i)
            next %= mod
            ret.append(next)
        return ret

    inv = generate_inv(10 ** 6, mod)

    ret = 0
    tmp_comb = 1

    pow25 = [pow(25, i, mod) for i in range(L+K)]
    pow26 = [pow(26, i, mod) for i in range(L + K)]
    for k in range(L, L+K+1):
        if k == L:
            tmp_comb = 1
        else:
            tmp_comb *= k-1
            tmp_comb %= mod
            tmp_comb *= inv[k-L]
            tmp_comb %= mod
        pow25_tmp = pow25[k-L]
        pow26_tmp = pow26[L+K-k]
        tmp_ret = pow25_tmp * pow26_tmp
        tmp_ret %= mod
        tmp_ret *= tmp_comb
        tmp_ret %= mod
        ret += tmp_ret
        ret %= mod
    print(ret)



if __name__ == "__main__":
    run()