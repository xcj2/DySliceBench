## tmp experiment
import math


def chinese_reminder(x1, y1, x2, y2):
    g = math.gcd(y1, y2)
    if (x2 - x1) % g != 0:
        return (float("inf"), float("inf"))
    else:
        K = (x2 - x1) // g
        y1, y2 = y1 // g, y2 // g
        t = -K * modinv(y2, y1)
        m = x2 + t * g * y2
        return (m % (g * y1 * y2), g * y1 * y2)


def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        return False
    else:
        return x % m


def divisors(X):
    res = set([])
    for i in range(1, X + 1):
        if i ** 2 > X:
            break
        else:
            if X % i == 0:
                res.add(i)
                res.add(X // i)
    return res


def main():

    N = int(input())
    d = divisors(2*N)
    ans = 10 ** 20
    for n in d:
        u, v = n, (2*N) // n
        if math.gcd(u, v) == 1:
            v, m = chinese_reminder(0, u, v-1, v)
            if v == 0:
                ans = min(m, ans)
            else:
                ans = min(v, ans)
    print(ans)


if __name__ == "__main__":
    main()
