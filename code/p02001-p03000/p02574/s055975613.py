import bisect, copy, heapq, math, sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
def celi(a,b):
    return -(-a//b)
sys.setrecursionlimit(5000000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n=int(input())
a=list(map(int,input().split()))
pc="pairwise coprime"
sc="setwise coprime"
nc="not coprime"

tmp=a[0]
for i in range(n):
    tmp=math.gcd(tmp,a[i])
if tmp!=1:
    print(nc)
    exit()

a.sort()

def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

def factorize(N,prime_list):  # prime_listに素数のリストをぶち込め！
    lst = []
    for p in prime_list:
        if p * p > N:
            break
        while N % p == 0:
            N //= p
            lst.append(p)
    if N > 1:
        lst.append(N)
    return lst

plst=primes(1000000)
dic={}
for i in range(n):
    fac=factorize(a[i],plst)
    for j in fac:
        if j in dic:
            print(sc)
            exit()
    for j in fac:
        dic[j]=1
print(pc)