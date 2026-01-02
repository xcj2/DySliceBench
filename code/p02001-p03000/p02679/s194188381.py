import sys
from collections import defaultdict
from functools import lru_cache

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

MOD = 10**9 + 7
P = 2 ** 61 - 1

N = int(readline())
m = map(int, read().split())
A, B = zip(*zip(m, m))

pow2 = [1] * (N + 10)
for n in range(1, N + 10):
    pow2[n] = pow2[n - 1] * 2 % MOD

@lru_cache(None)
def inv_mod(a):
    b = P
    u, v = 1, 0
    while a:
        t = b // a
        a, b = b - t * a, a
        u, v = v - t * u, u
    if b < 0:
        v = -v
    return v % P

def to_key(a, b):
    if a == 0:
        return -1
    x = inv_mod(a) * b % P
    return x

def pair_key(key):
    if key == -1:
        return 0
    if key == 0:
        return -1
    return P - inv_mod(key)
  
counter = defaultdict(int)
origin = 0
for a, b in zip(A, B):
    if a == b == 0:
        origin += 1
        continue
    key = to_key(a, b)
    counter[key] += 1

answer = origin
k = 1
for key, cnt in counter.items():
    key1 = pair_key(key)
    if key1 not in counter:
        k *= pow(2, cnt, MOD)
    elif key < key1:
        x, y = cnt, counter[key1]
        k *= pow(2, x, MOD) + pow(2, y, MOD) - 1
    k %= MOD
answer += k - 1
answer %= MOD
print(answer)
