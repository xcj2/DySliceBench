MOD = 1000000007

def modinv(a, m):
    b, u, v = m, 1, 0
    while b != 0:
        t = a // b
        a -= t * b
        a, b = b, a

        u -= t * v
        u, v = v, u
    u %= m
    if u < 0:
        u += m
    return u

a, b = 12345678900000, 100000
a %= MOD
#print(a * modinv(b, MOD) % MOD)

def solve(x, y):
    if (x + y) % 3 != 0:
        return 0
    m = (x + y) // 3
    #print(m, (x, y))
    if x < m:
        return 0
    n = m 
    k = x - m
    return C2(n, k)

def C2(n, k):
    d = 1
    for i in range(n-k+1, n+1):
        d *= i 
        d %= MOD
    r = 1
    for i in range(1, k+1):
        r *= i 
        r %= MOD
    return (d * modinv(r, MOD)) % MOD



def test(x, y):
    print((x,y), solve(x,y))
    assert solve(x,y) == solve(y,x)

x, y = map(int, input().split())
if x > y:
    x, y = y, x
answer = solve(x, y) % MOD
print(answer)
