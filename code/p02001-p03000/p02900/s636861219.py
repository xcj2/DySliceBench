from copy import deepcopy
from sys import exit,setrecursionlimit
import math
from collections import defaultdict,Counter,deque
from fractions import Fraction as frac
import bisect
import sys
import logging
import heapq
logging.basicConfig(level=logging.DEBUG)

input = sys.stdin.readline

setrecursionlimit(1000000)

MOD = 10**9+7

def main():
    A,B=[int(x) for x in input().split()]

    max_gcd=gcd([A,B])
    P=prime_factor(max_gcd)
    P2=set(P)
    print(len(P2)+1)

def gcd(l):
	x = l.pop()
	y = l.pop()
	while(x%y!=0):
		z = x%y
		x = y
		y = z
	l.append(min(x,y))
	return gcd(l) if len(l) > 1 else l[0]

def primes(n):
    ass = []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    for i in range(len(is_prime)):
        if is_prime[i]:
            ass.append(i)
    return ass

def divisor(n):
    ass = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            ass.append(i)
            if i**2 == n:
                continue
            ass.append(n//i)
    return ass #sortされていない

def prime_factor(n):
    ass = []
    for i in range(2,int(n**0.5)+1):
        while n % i==0:
            ass.append(i)
            n = n//i
    if n != 1:
        ass.append(n)
    return ass

main()