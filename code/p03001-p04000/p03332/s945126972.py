import numpy as np

mod = 998244353


def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    c = a % b
    return gcd(b, c)


def ii():
    return int(input())


def lii():
    return list(map(int, input().split(' ')))


def lvi(N):
    l = []
    for _ in range(N):
        l.append(ii())
    return l


def lv(N):
    l = []
    for _ in range(N):
        l.append(input())
    return l


def lcm(a, b):
    """
    最小公倍数
    """
    return a * b / gcd(a,b)


# def main_old():
#     N, A, B, K = lii()
#     dp = np.zeros([N+1, K+1])
#     dp[:, 0] = 1
#     for n in range(1, N+1):
#         for k in range(K+1):
#             c = dp[n-1][k]
#             if k - A >= 0: c += dp[n-1][k-A]
#             if k - B >= 0: c += dp[n-1][k-B]
#             if k - (A+B) >= 0: c += dp[n-1][k-(A+B)]
#             dp[n][k] = c
#
#     print(int(dp[N][K]) % mod)


def solve_eucl(A, B, K, N):
    for _x in range(N):
        if (K - A * _x) % B == 0:
            x = _x
            y = (K - A * _x) // B
            return x, y


def modinv(a, m):
    orgm = m
    x, lastx, y, lasty = 0, 1, 1, 0
    while m:
        a, (quotient, m) = m, divmod(a, m)
        x, lastx = lastx - quotient * x, x
        y, lasty = lasty - quotient * y, y
    if a != 1:
        raise ValueError
    return lastx % orgm


def fastcombmod(m, n):
    nn = min(n, m - n)
    num = 1
    div = 1
    for i in range(nn):
        num *= m - i
        if num > mod:
            num %= mod
        div *= i + 1
        if div > mod:
            div %= mod
    return (num * modinv(div, mod)) % mod


def combmod_table(m):
    num = 1
    div = 1
    t = [1]
    for i in range(m // 2 ):
        num *= m - i
        if num > mod:
            num %= mod
        div *= i + 1
        if div > mod:
            div %= mod

        t.append((num * modinv(div, mod)) % mod)

    return t


def main():
    N, A, B, K = lii()
    if K == 0: return 1

    d = gcd(gcd(A, B), K)
    if d > 1:
        A = A // d
        B = B // d
        K = K // d

    # x, y = solve_eucl(A, B, K, N)
    #
    # C = int(lcm(A, B))
    # ans = 0
    # p = x
    # while True:
    #     q = (K - A * p) // B
    #     if q <= 0:
    #         break
    #
    #     ans = (ans + fastcombmod(N, p) * fastcombmod(N, q)) % mod
    #     p += C // A
    #     if p > N:
    #         break
    #
    # return ans
    ans = 0
    ct = combmod_table(N)
    for x in range(N+1):
        y, m = divmod(K - A * x, B)
        if m == 0 and 0 <= y <= N:
            ans = ans + ct[min(x, N-x)] * ct[min(y, N-y)]
            ans = ans % mod
    return ans

if __name__ == '__main__':
    print(main())