import math
import bisect
import collections
import itertools
import heapq
import string
import sys
sys.setrecursionlimit(10**9)
def gcd(a,b):return math.gcd #最大公約数
def lcm(a,b):return (a*b) // math.gcd(a,b) #最小公倍数
def iin(): return int(input()) #整数読み込み
def isn(): return input().split() #文字列読み込み
def imn(): return map(int, input().split()) #整数map取得
def iln(): return list(map(int, input().split())) #整数リスト取得
def iln_s(): return sorted(iln()) # 昇順の整数リスト取得
def iln_r(): return sorted(iln(), reverse=True) # 降順の整数リスト取得
def join(l, s=''): return s.join(l) #リストを文字列に変換
def perm(l, n): return itertools.permutations(l, n) # 順列取得
def comb(l, n): return itertools.combinations(l, n) # 組み合わせ取得
def divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i: divisors.append(n//i)
    return divisors
def is_prime(n):
    if n == 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False 
    return True
def primes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if not is_prime[i]: continue
        for j in range(i * 2, n + 1, i): is_prime[j] = False
    return [i for i in range(n+1) if is_prime[i]]
def sieve_of_e(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if not is_prime[i]: continue
        for j in range(i * 2, n+1, i): is_prime[j] = False
    return is_prime

N = iin()
a = iln()
if sum(a) == 0:
    print('Yes')
    exit()

if N % 3 != 0:
    print('No')
else:
    d = {}
    for i in range(N):
        if a[i] not in d.keys():
            d[a[i]] = 1
        else:
            d[a[i]] += 1
    if len(d) == 3:
        keys = list(d.keys())
        values = list(d.values())
        if values[0] == values[1] == values[2] and keys[0] ^ keys[1] == keys[2]:
            print('Yes')
        else:
            print('No')
    elif len(d) == 2:
        if 0 in d.keys() and d[0] == N//3:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
