import sys
from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

MOD = 10**9 + 7
P = 2 ** 127 - 1

N = int(readline())
m = map(int, read().split())
A, B = zip(*zip(m, m))

pow2 = [1] * (N + 10)
for n in range(1, N + 10):
    pow2[n] = pow2[n - 1] * 2 % MOD

def mod_P(x):
    if x < 0:
        x += P
    high = x >> 127
    low = x & P
    x = low + high
    if x >= P:
        x -= P
    return x

def inv_mod(a):
    b = P
    u, v = 1, 0
    while a:
        q, r = divmod(b, a)
        a, b = r, a
        u, v = v - q * u, u
    if b < 0:
        v = -v
    if v < 0:
        v += P
    return v

pair_key = {0:-1, -1:0}

def to_key(a, b):
    if a == 0:
        return -1
    if b == 0:
        return 0
    
    x = mod_P(inv_mod(a) * abs(b))
    if b < 0:
        x = P - x
    y = P - mod_P(inv_mod(b) * abs(a))
    if a < 0:
        y = P - y
    pair_key[x] = y
    return x

  
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
    key1 = pair_key[key]
    if key1 not in counter:
        k *= pow2[cnt]
    elif key < key1:
        x, y = cnt, counter[key1]
        k *= pow2[x] + pow2[y] - 1
    k %= MOD
answer += k - 1
answer %= MOD
print(answer)
