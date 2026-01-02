N = int(input())

from collections import Counter
import math

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

L = []
for i in range(1, N+1):
    prime = prime_factorize(i)
#    print(i, prime)
    L += prime
C = Counter(L)
#print(C)


def count_n(C, n):
    return [v >= n for v in C.values()].count(True)

count_4 = count_n(C, 4)
count_2 = count_n(C, 2)
count_14 = count_n(C, 14)
count_24 = count_n(C, 24)
count_74 = count_n(C, 74)


c4_442 = count_4
c2_442 = count_2 - 2

if c4_442 < 2 or c2_442 < 1:
    ans442 = 0
else:
    ans442 = combinations_count(c4_442, 2)*combinations_count(c2_442, 1)

c14_144 = count_14
c4_144 = count_4 - 1
if c14_144 < 1 or c4_144 < 1:
    ans144 = 0
else:
    ans144 = combinations_count(c14_144, 1)*combinations_count(c4_144, 1)

c24_242 = count_24
c2_242 = count_2 - 1
if c24_242 < 1 or c2_242 < 1:
    ans242 = 0
else:
    ans242 = combinations_count(c24_242, 1)*combinations_count(c2_242, 1)
    
c74_74 = count_74
if c74_74 < 1:
    ans74 = 0
else:
    ans74 = combinations_count(c74_74, 1)
    
print(ans442+ans144+ans242+ans74)
