#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

a,b = map(int,input().split())
def prime_factor(n):
    ass = []
    for i in range(2,int(n**0.5)+1):
        count=0
        while n % i==0:
            count+=1
            n = n//i
        if count!=0:
            ass.append((i,count))
    if n != 1:
        ass.append((n,1))
    return ass
def gcd(a, b):
    while(b != 0):
        a, b = b, a % b
    return a
    
def lcm(m,n):
    return (m*n)//gcd(m,n)

ab = gcd(a,b)
primes = prime_factor(ab)
print(len(primes)+1)