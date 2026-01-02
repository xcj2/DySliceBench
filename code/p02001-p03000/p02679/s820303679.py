import math
import itertools

n = int(input())
mod = 1000000007

def Sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0

allZeros = 0
vectors = dict()


def add_positive(_):
    if _ not in vectors:
        vectors[_] = (1, 0)
    else:
        vectors[_] = (vectors[_][0] + 1, vectors[_][1])


def add_negative(_):
    if _ not in vectors:
        vectors[_] = (0, 1)
    else:
        vectors[_] = (vectors[_][0], vectors[_][1] + 1)


for i in range(n):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        allZeros += 1
        continue
    gcd = math.gcd(a, b)

    key = (0, 0)
    if a == 0:
        key = (1, 0)
        add_negative(key)
    elif b == 0:
        key = (1, 0)
        add_positive(key)

    elif Sign(a) * Sign(b) > 0:
        key = (abs(a) // gcd, abs(b) // gcd)
        add_positive(key)
    else:
        key = (abs(b) // gcd, abs(a) // gcd)
        add_negative(key)

total = 1
for vec in vectors.values():

    total *= ((2**(vec[0]))
              + (2**(vec[1])) - 1) % mod

print(((total- 1) % mod + allZeros % mod) % mod)