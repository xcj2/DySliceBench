def gcd(a, b):
    a, b = max(a, b), min(a, b)
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    N = int(input())
    MAX = 3501
    for h in range(1, MAX):
        gcdNh = gcd(N, h)
        for n in range(1, MAX):
            gcdNhn = gcd(gcdNh, n)
            denom = N * h * n // gcdNhn**2
            num = 4 * denom // N - denom // h - denom // n
            if num > 0 and denom % num == 0:
                w = denom // num
                print(h, n, w)
                return


if __name__ == "__main__":
    main()
