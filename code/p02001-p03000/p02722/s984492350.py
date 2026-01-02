#input
N = int(input())

#output
#ある整数nの素因数を列挙
import math
from collections import Counter
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

def sub_div(n, k):
    if k == 1:
        return n
    while n >= k:
        if n % k == 0:
            n = n//k
        else:
            n = n % k
    return n

a = Counter(prime_factors(N))
b = Counter(prime_factors(N-1))
c = make_divisors(N)

answer = 1
for value in b.values():
    answer *= (value+1)

answer -= 1

for x in c:
    if sub_div(N, x) == 1:
        answer += 1

print(answer)