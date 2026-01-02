
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
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9+7
    norm = 0
    for a in A:
        norm += a**2
        # norm = norm%mod
    ans = ((sum(A))**2 - norm) % mod
    ans = ans * modinv(2, mod)
    print(int(ans%mod))


if __name__ == '__main__':
    main()