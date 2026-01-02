mod = 1000000007;

def bin(b, m):
    a = b;
    n = m;
    res = 1;
    while n > 0:
        if n % 2 == 1:
            res = (res * a) % mod;
        a = (a * a) % mod;
        n //= 2;
    return res;

def fact(x):
    res = 1;
    for i in range(1, x + 1):
        res = (res * i) % mod;
    return res;

def inv(x):
    return bin(x, mod - 2);

def cnk(n, k):
    res = 1;
    for i in range(n - k + 1, n + 1):
        res = (res * i) % mod;
    return (res * inv(fact(k))) % mod;

n, a, b  = (int(i) for i in input().split());

ans = (bin(2, n) - 1 - cnk(n, a) - cnk(n, b) + 3 * mod) % mod;
#print(bin(2, n), cnk(n, a), cnk(n, b));
print(ans);
