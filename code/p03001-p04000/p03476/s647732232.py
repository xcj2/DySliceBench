from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations, accumulate, product, combinations_with_replacement
import sys
import bisect
import string
import math
import time

def I(): return int(input())
def S(): return input()
def MI(): return map(int, input().split())
def MS(): return map(str, input().split())
def LI(): return [int(i) for i in input().split()]
def LI_(): return [int(i)-1 for i in input().split()]
def StoI(): return [ord(i)-97 for i in input()]
def ItoS(nn): return chr(nn+97)
def input(): return sys.stdin.readline().rstrip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]


yn = ['Yes', 'No']
YN = ['YES', 'NO']
MOD = 10**9+7
inf = float('inf')
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)


show_flg = False
# show_flg = True

def primes(n):
    is_prime = [1] * (n + 1)
    is_prime[0] = 0
    is_prime[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = 0
    return is_prime


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
             return False
    return True


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def coprime(a, b):
    return gcd(a, b) == 1


def main():
    Q = I()
    l = [0] * Q
    r = [0] * Q
    MX = 10**5+1

    for i in range(Q):
        l[i], r[i] = MI()

    primes_nums = primes(MX)
    likes_2017 = [int(i % 2 == 1 and primes_nums[i] and primes_nums[(i+1)//2]) for i in range(MX)]
    likes_2017_acc = list(accumulate(likes_2017))
    # print(likes_2017)

    for i in range(Q):
        ans = likes_2017_acc[r[i]] - likes_2017_acc[l[i]-1]
        print(ans)


if __name__ == '__main__':
    main()
