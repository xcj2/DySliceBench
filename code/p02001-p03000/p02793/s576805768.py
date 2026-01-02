MOD = 10**9+7
n = int(input())
a = list(map(int, input().split()))

def make_inv(n, mod=10**9+7):
    inv = [0, 1] + [0] * (n-2)
    for i in range(2, n):
        inv[i] = mod - inv[mod % i] * (mod//i) % mod
    return inv

def get_primes(lim):
    table = [True] * (lim+1)
    table[0:2] = False, False
    for i in range(2, int(lim**0.5)+1):
        if not table[i]: continue
        for j in range(i*2, lim+1, i):
            table[j] = False
    return [i for i in range(lim+1) if table[i]]

def factorize(x, primes):
    res = []
    for p in primes:
        if p ** 2 > x: break
        cnt = 0
        while not x % p:
            x //= p
            cnt += 1
        if cnt: res.append((p, cnt))
    if x > 1: res.append((x, 1))
    return res

inv = make_inv(10**6+1)
table = [0] * (10**6+1)
primes = get_primes(10**4)

for x in a:
    for i, num in factorize(x, primes):
        table[i] = max(table[i], num)

lcm = 1
for x, num in enumerate(table):
    if not num: continue 
    lcm *= pow(x, num, MOD)
    lcm %= MOD

ans = 0
for x in a:
    ans += lcm * inv[x]
    ans %= MOD

print(ans)
