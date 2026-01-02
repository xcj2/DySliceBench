def make_prime_factors_compress(n: int):
    """自然数nの素因数を列挙した圧縮済みリストを出力する
    計算量：O(sqrt(N))
    入出力例：156 -> [(2, 2), (3, 1), (13, 1)]
    """
    prime_factors = []
    for k in range(2, int(n**0.5) + 1):
        cnt = 0
        while n % k == 0:
            cnt += 1
            n = n // k
        if cnt != 0:
            prime_factors.append((k, cnt))
    if n != 1:
        prime_factors.append((n, 1))
    return prime_factors

def gcd(a: int, b: int) -> int:
    """a, bの最大公約数(greatest common divisor: GCD)を求める
    計算量: O(log(min(a, b)))
    """
    if b == 0:
        return a
    return gcd(b, a%b)


def lcm(a: int, b: int) -> int:
    """a, bの最小公倍数(least common multiple: LCM)を求める
    計算量: O(log(min(a, b)))
    """
    return (a * b) // gcd(a, b)

  
a, b = map(int, input().split())
gcd_ = gcd(a, b)
print(len(make_prime_factors_compress(gcd_)) + 1)