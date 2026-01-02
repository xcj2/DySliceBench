


def factorial(x, modp):
    curr = 1
    for i in range(1, x + 1):
        curr *= i
        curr %= modp
    return curr


def power(x, n, modp):
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
    
    return k * x % modp


def submit():
    x, y = map(int, input().split())
    
    # (i, j) -> (i + 1, j + 2)の移動方法をs回
    # (i, j) -> (i + 2, j + 1)の移動方法をt回行なったとする
    # t = Y - 2s, s = (2Y - X) / 3となる
    s = 2*y - x
    if s < 0 or s % 3 != 0: # 移動方法なし
        print(0)
        return
    s //= 3

    t = y - 2*s
    if t < 0: # 移動方法なし
        print(0)
        return

    # 全移動n = s + t中のs移動のパターンを数え上げれば良い
    # n_C_sを求めれば良い
    # n! / s! (n - s)! ≡ n! (s!)^modp-2 ((n - s)!)^modp-2
    n = s + t
    modp = 10**9 + 7
    ans = factorial(n, modp) * power((factorial(s, modp)), modp - 2, modp) * power(factorial(n - s, modp), modp - 2, modp)
    ans %= modp
    print(ans)
    
    
if __name__ == "__main__":
    submit()