import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

def factorization(n):
   arr = []
   temp = n
   for i in range(2, int(-(-n**0.5//1))+1):
       if temp%i==0:
           cnt=0
           while temp%i==0:
               cnt+=1
               temp //= i
           arr.append([i, cnt])
   if temp!=1:
       arr.append([temp, 1])
   if arr==[]:
       arr.append([n, 1])
   return arr

factorial = [1]
for i in range(1, 1000000):
	factorial.append(factorial[i-1] * i % mod)
 
def power(x, y):
	if y == 0:
		return 1
	elif y == 1:
		return x % mod
	elif y % 2 == 0:
		return power(x, int(y/2)) ** 2 % mod
	else:
		return power(x, int((y-1)/2)) ** 2 * x % mod
def C(n, r):
	return (((factorial[n] * x_inv[r]) % mod) * x_inv[n-r]) % mod
 
x_inv = [0] * (1000000)
x_inv[-1] = power(factorial[-1], mod-2)
for i in range(1000000-2, -1, -1):
	x_inv[i] = x_inv[i+1] * (i+1) % mod

N, M = MAP()

fact_M = factorization(M)

ans = 1
if M == 1:
	print(1)
else:
	for n in fact_M:
		ans = (ans*C(n[1]+N-1, n[1]))%mod
	print(ans)
