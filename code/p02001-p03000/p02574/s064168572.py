import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

import itertools
import collections

def prime_factor_table(n):
    table = [0] * (n + 1)
    
    for i in range(2, n + 1):
        if table[i] == 0:
            for j in range(i + i, n + 1, i):
                table[j] = i
    
    return table

def prime_factor(n, prime_factor_table):
    prime_count = collections.Counter()
    
    while prime_factor_table[n] != 0:
        prime_count[prime_factor_table[n]] += 1
        n //= prime_factor_table[n]
    prime_count[n] += 1
    
    return prime_count

n = int(input())
a = list(map(int,input().split()))

# pairwise coprime -> それぞれがすべて互いに素
# setwise coprime -> 互いに素でないのは混じっているが全体のgcdは1

if gcd_list(a) != 1:
    print("not coprime")
    exit()

pft = prime_factor_table(10**6)
pf = [0]*(10**6+1)

for i in a:
    if i == 1:
        continue
    # print(prime_factor(i, pft).keys())
    for j in prime_factor(i, pft).keys():
        if pf[j] == 1:
            print("setwise coprime")
            exit()
        pf[j] += 1

print("pairwise coprime")