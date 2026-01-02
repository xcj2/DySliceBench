mod = 10**9+7
n = int(input())
num = [ int(v) for v in input().split() ]

def gcd(a,b):
    if a < b:
        a, b = b, a
    while b >= 1:
        a, b = b, a % b
    return a
def lcm(a,b):
	return a * b // gcd(a,b)

def shave(n):
    if n < 2:
        return []
    else:
        n_root = int(n**0.5)
        candidate = [i for i in range(3, n+1, 2)]
        for i in range(3, n_root+2, 2):
            candidate = [j for j in candidate if j == i or j % i != 0]
        candidate = [2] + candidate
        return candidate

d = {}
prime_list = shave(10**3)
for i in prime_list:
    d[i] = 0

def prime_factorization(x):

    for i in prime_list:
        if x == 1:
            break
        elif x % i == 0:
            q = 0
            while x % i == 0:
                x //= i
                q += 1
            d[i] = max(d[i], q)
    if x != 1:
        d[x] = 1
    return 

for i in num:
    prime_factorization(i)

l = 1
for i in d:
    l *= pow(i, d[i], mod)
    l %= mod

ans = 0
for i in num:
    a = l * pow(i, mod-2, mod)
    ans += a
    ans %= mod
print(ans)