



def fact(n, r, modp):
    """
    n ~ (n - r + 1)の積 % modpを求める
    """
    curr = n % modp
    for x in range(n - r + 1, n):
        curr *= x
        curr %= modp
    return curr


def power(x, n, modp):
    """
    modつき累乗
    return x^n % modp
    """
    if n == 0:
        return 1

    k = 1
    while n > 1:
        if n % 2:
            k *= x
            k %= modp
        x *= x
        x %= modp
        n //= 2

    return (k * x) % modp


def combination(n, r, modp):
    """
    modつき組み合わせ計算
    return n_C_r % modp
    """ 
    # フェルマーの小定理を利用
    num = fact(n, r, modp)
    den = fact(r, r, modp)

    c = num * power(den, modp - 2, modp)
    return c % modp


def submit():
    n, a, b = map(int, input().split())
    modp = 1000000007
    ans = power(2, n, modp) - combination(n, a, modp) - \
          combination(n, b, modp) - 1
    print(ans % modp)


if __name__ == "__main__":
    submit()