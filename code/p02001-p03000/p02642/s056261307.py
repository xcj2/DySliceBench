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
def print_matrix(mat):
    for i in range(len(mat)):
        print(*['IINF' if v == IINF else "{:0=4}".format(v) for v in mat[i]])


yn = {False: 'No', True: 'Yes'}
YN = {False: 'NO', True: 'YES'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**19
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
show_flg = False
# show_flg = True


# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)


# def lcm(a, b):
#     return a*b // gcd(a, b)


# def good(A, N):
#     # A = sorted(A)
#     ans = A[0]
#     # for i in range(1, N):
#     #     ans = fractions.gcd(A[i], ans)
#     for i in range(1, N):
#         ans = lcm(ans, A[i])
#     return ans

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


def factorization(n):
    if n <= 1:
        return []

    ret = []
    while n > 2 and n % 2 == 0:
        ret.append(2)
        n //= 2
    i = 3
    while i <= math.sqrt(n):
        if n % i == 0:
            ret.append(i)
            n //= i
        else:
            i += 2
    ret.append(n)
    return ret


def main():
    N = I()
    A = LI()
    MX = 2 * 10**6
    ans = []

    # for i in range(N):
    #     n = []
    #     for j in range(N):
    #         if i == j:
    #             continue
    #         n.append(A[i] % A[j] != 0)
    #     if all(n):
    #         ans.append(i+1)

    # print(len(ans))
    # print([A[i-1] for i in ans])

    a_map = Counter(A)

    n = MX
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = 1 in a_map
    for i in range(1, 10**6 + 1):
        if not is_prime[i]:
            continue
        if i not in a_map:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False

    ans = 0
    for i in range(N):
        if is_prime[A[i]] and a_map[A[i]] == 1:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
