# from fractions import gcd
# from datetime import date, timedelta
# from heapq import *
# import heapq
# import math
# from collections import defaultdict, Counter, deque
# from bisect import *
# import itertools
# import fractions
# # import sys
# sys.setrecursionlimit(10 ** 7)
# MOD = 10 ** 9 + 7
# input = sys.stdin.readline


# def lcm(a, b):
#     return a * b / fractions.gcd(a, b)


# def make_divisors(n):
#     divisors = []
#     for i in range(1, int(n**0.5)+1):
#         if n % i == 0:
#             divisors.append(i)
#             if i != n // i:
#                 divisors.append(n//i)

#     # divisors.sort()
#     return divisors


# def factorize(n):
#     fct = []  # prime factor
#     b, e = 2, 0  # base, exponent
#     while b * b <= n:
#         while n % b == 0:
#             n = n // b
#             e = e + 1
#         if e > 0:
#             fct.append((b, e))
#         b, e = b + 1, 0
#     if n > 1:
#         fct.append((n, 1))
#     return fct


# def is_prime(n):
#     if n == 1:
#         return False

#     for k in range(2, int(math.sqrt(n)) + 1):
#         if n % k == 0:
#             return False

#     return True


# def primes(n):
#     is_prime = [True] * (n + 1)
#     is_prime[0] = False
#     is_prime[1] = False
#     for i in range(2, int(n**0.5) + 1):
#         if not is_prime[i]:
#             continue
#         for j in range(i * 2, n + 1, i):
#             is_prime[j] = False
#     return [i for i in range(n + 1) if is_prime[i]]

# def modpow(a, n, mod):
#     res = 1
#     while n > 0:
#         if n & 1:
#             res = res * a % mod
#         a = a * a % mod
#         n >>= 1
#     return res


# def modinv(a, mod):
#     return modpow(a, mod - 2, mod)


# def cnk(a, b):
#     MOD = 10**9+7
#     ret = 1
#     for i in range(b):
#         ret *= (a-i)
#         ret %= MOD
#         ret = ret * modinv(i+1, MOD) % MOD
#     return ret


# class UnionFind:
#     def __init__(self, n):
#         self.sz = [-1 for i in range(n)]

#     # 検索
#     def find(self, x):
#         if self.sz[x] < 0:
#             return x
#         else:
#             self.sz[x] = self.find(self.sz[x])
#             return self.sz[x]

#     # 併合
#     def union(self, x, y):
#         x = self.find(x)
#         y = self.find(y)
#         if x == y:
#             return False
#         if self.sz[x] > self.sz[y]:
#             x, y = y, x
#         self.sz[x] += self.sz[y]
#         self.sz[y] = x

#     # 同じ集合に属するか判定
#     def same(self, x, y):
#         return self.find(x) == self.find(y)

#     # xが含まれている集合のサイズを求める
#     def size(self, x):
#         return -self.sz[self.find(x)]

# class WeightedUnionFind:
#     def __init__(self, n):
#         self.par = [i for i in range(n+1)]
#         self.rank = [0] * (n+1)
#         # 根への距離を管理
#         self.weight = [0] * (n+1)

#     # 検索
#     def find(self, x):
#         if self.par[x] == x:
#             return x
#         else:
#             y = self.find(self.par[x])
#             # 親への重みを追加しながら根まで走査
#             self.weight[x] += self.weight[self.par[x]]
#             self.par[x] = y
#             return y

#     # 併合
#     def union(self, x, y, w):
#         rx = self.find(x)
#         ry = self.find(y)
#         # xの木の高さ < yの木の高さ
#         if self.rank[rx] < self.rank[ry]:
#             self.par[rx] = ry
#             self.weight[rx] = w - self.weight[x] + self.weight[y]
#         # xの木の高さ ≧ yの木の高さ
#         else:
#             self.par[ry] = rx
#             self.weight[ry] = -w - self.weight[y] + self.weight[x]
#             # 木の高さが同じだった場合の処理
#             if self.rank[rx] == self.rank[ry]:
#                 self.rank[rx] += 1

#     # 同じ集合に属するか
#     def same(self, x, y):
#         return self.find(x) == self.find(y)

#     # xからyへのコスト
#     def diff(self, x, y):
#         return self.weight[x] - self.weight[y]


class manacher:

    def __init__(self, l):
        self.n = len(l)
        self.m = 2*self.n+1
        self.d = ['&']*self.m
        self.r = [0]*self.m
        for i in range(self.n):
            self.d[2*i+1] = l[i]
        self.make_r()

    def make_r(self):
        i, j = 0, 0
        while i < self.m:
            while j <= i < self.m-j and self.d[i-j] == self.d[i+j]:
                j += 1
            self.r[i] = j
            k = 1
            while k <= i < self.m-k and k+self.r[i-k] < j:
                self.r[i+k] = self.r[i-k]
                k += 1
            i += k
            j -= k

    def judge(self, start, end):
        center = start+end
        return 2 * end - 1 < center + self.r[center]


def main():
    a, b, c = map(int, input().split())
    if c - a - b < 0:
        print("No")
        exit()
        
    left = 4 * a * b
    right = (c - a - b)** 2
    if left <right:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
