# ρ法でとおるかためす。

# 参考1: https://qiita.com/Kiri8128/items/eca965fe86ea5f4cbb98
# 参考2: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
# 参考3: https://ja.wikipedia.org/wiki/%E3%83%9D%E3%83%A9%E3%83%BC%E3%83%89%E3%83%BB%E3%83%AD%E3%83%BC%E7%B4%A0%E5%9B%A0%E6%95%B0%E5%88%86%E8%A7%A3%E6%B3%95


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def is_prime(n):
    "Miller Rabin primality test. 2 <= n <= 2 ** 64 is required"
    if n % 2 == 0:
        return n == 2
    d = n - 1
    r = (d & -d).bit_length() - 1
    d >>= r

    # witnesses をいい感じに決める。
    if n < 2152302898747:
        if n < 9080191:
            if n < 2047:
                witnesses = [2]
            else:
                witnesses = [31, 73]
        else:
            if n < 4759123141:
                witnesses = [2, 7, 61]
            else:
                witnesses = [2, 3, 5, 7, 11]
    else:
        if n < 341550071728321:
            if n < 3474749660383:
                witnesses = [2, 3, 5, 7, 11, 13]
            else:
                witnesses = [2, 3, 5, 7, 11, 13, 17]
        else:
            if n < 3825123056546413051:
                witnesses = [2, 3, 5, 7, 11, 13, 17, 19]
            else:
                witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    # witnesses の決定終了

    for a in witnesses:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x *= x
            x %= n
            if x == n - 1:
                break
        else:
            return False
    return True


def find_factor(n):
    "Find a non-trivial factor of n by using Pollard's rho algorithm."
    m = int(n ** 0.125) + 1
    c = 1
    while True:
        y = 1
        r = 1
        q = 1
        g = 1
        while g == 1:
            x = y
            for _ in range(r):
                y = (y * y + c) % n
            for k in range(0, r, m):
                ys = y
                for _ in range(m):
                    y = (y * y + c) % n
                    q = q * (x - y) % n
                g = gcd(q, n)
                if g != 1:
                    break
            else:  # 残りの k から r までをやる
                ys = y
                for _ in range(r-k):
                    y = (y * y + c) % n
                    q = q * (x - y) % n
                g = gcd(q, n)
            r *= 2

        if g == n:
            g = 1
            while g == 1:
                ys = (ys * ys + c) % n
                g = gcd(x - ys, n)

        if g == n:
            c += 1  # c を変えて続行。
        else:  # g は n の非自明な素因数。
            return g


def fac(n):
    "計算量は O(n ^ 1/4) 程度。"
    if n == 1:
        return []
    if is_prime(n):
        return [n]

    ret = []
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
        while n % p == 0:
            ret.append(p)
            n //= p
        if n == 1:
            return ret

    while n != 1 and not is_prime(n):
        f = find_factor(n)
        if is_prime(f):
            while n % f == 0:
                ret.append(f)
                n //= f
        elif is_prime(n // f):
            ret.append(n // f)
            n = f
        else:
            return sorted(ret + fac(f) + fac(n // f))

    if n == 1:
        return sorted(ret)
    else:
        ret.append(n)
        return sorted(ret)




N = int(input())
As = list(map(int, input().split()))

g = 0
for A in As:
    g = gcd(g, A)

if g != 1:
    print("not coprime")
    exit()

primes = set()
for A in As:
    ps = set(fac(A))
    if ps & primes:
        print("setwise coprime")
        exit()
    else:
        primes |= ps

print("pairwise coprime")
