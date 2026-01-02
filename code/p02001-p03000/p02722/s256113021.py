import sys, math
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial#, gcd
from bisect import bisect_left #bisect_left(list, value)
sys.setrecursionlimit(10**7)
enu = enumerate
MOD = 10**9+7
def input(): return sys.stdin.readline()[:-1]
def pri(x): print('\n'.join(map(str, x)))
def prime_decomposition(n):
    i = 2
    table = []
    while i*i <= n:
        while n%i == 0:
            n //= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table
def prime_decomposition2(n):
    i = 2
    table = defaultdict(int)
    while i*i <= n:
        while n%i == 0:
            n //= i
            table[i] += 1
        i += 1
    if n > 1:
        table[n] += 1
    return table
def make_divisor(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            divisors.append(i)
            if i != n//i:
                divisors.append(n//i)
    return divisors

N = int(input())
list_pd1 = make_divisor(N)
list_pd1.sort()
dict_pd2 = prime_decomposition2(N-1)
#print(N, ':', list_pd1)
#print(N-1, ':', dict_pd2)

cnt = 1

# -1 nohou
for val in dict_pd2.values():
    cnt *= (val+1)
cnt -= 1
#print(cnt)

for k in list_pd1[1:]:
    #print('k:', k)
    sN = N
    while sN >= k:
        if sN%k==0:
            sN //= k
        else:
            sN %= k
    if sN == 1:
        cnt += 1

print(cnt)

