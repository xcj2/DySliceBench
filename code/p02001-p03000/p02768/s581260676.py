# import sys
# sys.setrecursionlimit(10 ** 6)


def cmb2(n, r, mod):
    if n < r:
        return 0
    re = 1
    for i in range(n - r + 1, n + 1):
        re = (re * i) % mod
    for i in range(1, r + 1):
        re = (re * inverse(i, mod)) % mod
    return re % mod


def inverse(a, p):
    a_, p_ = a, p
    x, y = 1, 0
    while p_:
        t = a_ // p_
        a_ -= t * p_
        a_, p_ = p_, a_
        x -= t * y
        x, y = y, x
    x %= p
    return x


# from decorator import stop_watch
# 
# 
# @stop_watch
def solve(n, a, b):
    mod = 10 ** 9 + 7
    ans = pow(2, n, mod)
    ans = (ans - cmb2(n, a, mod)) % mod
    ans = (ans - cmb2(n, b, mod)) % mod
    ans -= 1  # remove zero flower pattern
    print(ans)


if __name__ == '__main__':
    n, a, b = map(int, input().split())
    solve(n, a, b)
