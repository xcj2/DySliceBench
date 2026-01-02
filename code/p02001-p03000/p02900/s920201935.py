from sys import stdin, setrecursionlimit


def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y)


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    input = stdin.buffer.readline
    a, b = map(int, input().split())

    g = gcd(a, b)

    ans = 0

    for i in range(1, int(g ** 0.5) + 1):
        if g % i == 0:
            if is_prime(i) or i == 1:
                ans += 1
            if is_prime(g // i) and i != g // i:
                ans += 1

    print(ans)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
