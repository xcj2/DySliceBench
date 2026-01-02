from collections import Counter


# 拡張ユークリッド互除法
# gcd(a,b) と ax + by = gcd(a,b) の最小整数解を返す
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def chineseRem(b1, m1, b2, m2):
    # 中国剰余定理
    # x ≡ b1 (mod m1) ∧ x ≡ b2 (mod m2) <=> x ≡ r (mod m)
    # となる(r. m)を返す
    # 解無しのとき(0, -1)
    d, p, q = egcd(m1, m2)
    if (b2 - b1) % d != 0:
        return 0, -1
    m = m1 * (m2 // d)  # m = lcm(m1, m2)
    tmp = (b2-b1) // d * p % (m2 // d)
    r = (b1 + m1 * tmp) % m
    return r, m


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


N = int(input())
p = prime_factorize(2*N)
c = Counter(p)

if N == 1:
    print(1)
    exit()

if len(c.keys()) == 1:
    print(N-1)
    exit()

d = [k ** v for k, v in c.items()]

m = len(d)

ans = N-1
for i in range(2 ** m):
    a, b = 1, 1
    for j in range(m):
        if (i >> j) & 1:
            a *= d[j]
        else:
            b *= d[j]

    if a == 1 or b == 1:
        continue

    ans = min(ans, chineseRem(0, a, b-1, b)[0])
    ans = min(ans, chineseRem(a-1, a, 0, b)[0])

print(ans)
