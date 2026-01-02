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

def primes(n):
    is_prime = [-1] * (n + 1)
    is_prime[1]=1
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]!=-1:
            continue
        for j in range(i * 2, n + 1, i):
            if is_prime[j]==-1:
                is_prime[j] = i
    for i in range(n):
        if is_prime[i+1]==-1:
            is_prime[i+1]=i+1
    return is_prime


def factorize(N,prime_list):  # prime_listに素数のリストをぶち込め！
    lst = []
    # if N==1:
    #     lst.append(1)
    while prime_list[N]!=1:
        lst.append(prime_list[N])
        N//=prime_list[N]
    return lst

tmp=a[0]
for i in range(n):
    tmp=math.gcd(tmp,a[i])
if tmp!=1:
    print("not coprime")
    exit()
dic={}
plst=primes(10**6)
for i in range(n):
    lst=factorize(a[i],plst)
    for j in lst:
        if j in dic:
            print("setwise coprime")
            exit()
    for j in lst:
        dic[j]=1
print("pairwise coprime")