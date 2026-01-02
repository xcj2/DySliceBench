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

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

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

N = int(input())
A_s = list(map(int, input().split()))
# A_s = [int(i+1) for i in range(N)]
pc = True
sc = True
M = {}
MAX = 0
TABLE = prime_factor_table(10**6+1)

for i,A in enumerate(A_s):
    L = prime_factor(A, TABLE)
    for l in L.keys():
        if l == 1:
            continue
        if l in M:
            # print()
            M[l] += 1
            pc = False
        else:
            M[l] = 1
        MAX = max(MAX, M[l])
    if not pc and MAX <= i:
        break
else:
    sc = False

if pc:
    print('pairwise coprime')
elif sc:
    print('setwise coprime')
else:
    print('not coprime')