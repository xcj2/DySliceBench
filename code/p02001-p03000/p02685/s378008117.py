

def diff_colors(x, m, modp):
    """
    長さxの列をm色で塗る
    このとき、連続して同じ色を使わないパターン数を数える
    """
    ans = m
    x -= 1
    while x:
        ans *= (m - 1)
        ans %= modp
        x -= 1
    return ans

def factorial(x, modp):
    fact = dict()
    fact[0] = 1
    curr = 1
    while curr <= 2 * x:
        fact[curr] = fact[curr - 1] * curr
        fact[curr] %= modp
        curr += 1
    return fact


def pow(x, k, modp):
    ans = 1
    while k:
        if k % 2:
            ans *= x
            ans %= modp
        x *= x
        x %= modp
        k //= 2
    return ans


def combi(fact, n, k, modp):
    ans = fact[n + k - 1]
    ans *= pow(fact[k], modp - 2, modp)
    ans %= modp
    ans *= pow(fact[n - 1], modp - 2, modp)
    ans %= modp
    return ans


def submit():
    n, m, k = map(int, input().split())
    modp = 998244353
    fact = factorial(n, modp)

    ans = 0
    base_pattern = diff_colors(n - k, m, modp)
    for i in range(k + 1):
        ans += base_pattern * combi(fact, n - (k - i), k - i, modp)
        ans %= modp
        base_pattern *= (m - 1)
        base_pattern %= modp

    print(ans)
    

if __name__ == "__main__":
    submit()    