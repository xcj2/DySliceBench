import sys
from itertools import count, accumulate
from operator import mul
from functools import reduce
lines = sys.stdin.readlines()

positions = [int(i) for i in lines[1].split(' ')]

distances = [ j - i for i, j in zip(positions, positions[1:])]

n = len(distances)
p = pow(10,9) + 7

factorials = [1] + list(accumulate(range(1,n + 1), lambda x, y: (x * y) % p))

combinations = dict()
def combination(i, j):
    j = min(j, i - j)
    if (i, j) in combinations:
        return combinations((i, j))
    else:
        return factorials[i] // (factorials [j] * factorials[i - j])

permutations = dict()
def permutation(i, j):
    if (i, j) in permutations:
        return permutations((i, j))
    else:
        return reduce(mul, range(j, i+1))

def modpow(a, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n = n >> 1
    return res

s = 0
result = 0
for d, i in zip(distances, count(1)):
    lt = i - 1
    gt = n - i
    i_inv = modpow(i, p-2, p)
    t = factorials[n] * i_inv
    s += t
    result += d * s

print(int(result % (pow(10,9) + 7)))