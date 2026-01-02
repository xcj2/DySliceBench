#%%
import sys
def input():
    return sys.stdin.readline().rstrip()

def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a//b, b, a%b
        x0, x1 = x1, x0 -q*x1
        y0, y1 = y1, y0 -q*y1
    return a, x0, y0

def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x %m

def main():
    X, Y = map(int, input().split())

    divider = 10**9 + 7

    m = 2 * X - Y
    n = 2 * Y - X

    if m%3 != 0 or n%3 != 0 or n < 0 or m < 0:
        print(0)
        return
    m //= 3
    n //= 3

    if m < n:
        m, n = n, m

    ans = 1
    for i in range(m+n, m, -1):
        ans *= i
        ans %= divider

    for i in range(n, 0, -1):
        ans *= modinv(i, divider)
        ans %= divider

    print(ans)

# %%
if __name__ == '__main__':
    main()

# %%
# from atcoder_test import doTest
# doTest("abc145","d",main)
