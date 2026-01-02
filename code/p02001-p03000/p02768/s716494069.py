n, a, b = [int(x) for x in input().split()]

M = 10 ** 9 + 7
# return 2 ** n % 10^9 + 7
def pow2(n):
    pow2s = [2]
    i = 1
    while 2 ** i <= n:
        pow2s.append(pow2s[-1] ** 2 % M)
        i += 1
    r = 1
    for i in range(len(pow2s)):
        if n & (1 << i) != 0:
            r = (r * pow2s[i]) % M
    return r

def fact(n):
    r = 1
    for i in range(1, n + 1):
        r = (r * i) % M
    return r

def inv(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return x0

def comb(n, k):
    r1 = 1
    for i in range(k):
        r1 = r1 * (n - i) % M
    r2 = 1
    for i in range(k):
        r2 = r2 * (i + 1) % M
    return r1 * inv(r2, M) % M
r = pow2(n) - 1 - comb(n, a) - comb(n, b)
while r < 0:
    r += M
print(r)

    
