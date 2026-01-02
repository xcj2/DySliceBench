
def isPrime(n):
    n = abs(n)
    if n == 2:
        return True
    if n < 2 or n & 1 == 0:
        return False
    return pow(2, n - 1, n) == 1

def gcd(n, m):
    while m:
        n, m = m, n % m
    return n

def lcm(n, m):
    return n * m // gcd(n, m)

def main():
    a, b, c = list(map(lambda x: int(x), input().split()))
    ans = 0
    for i in range(1000000 + 1):
        login_coin = i * a
        bonus_coin = i // 7 * b
        total = login_coin + bonus_coin
        if total >= c:
            ans = i
            break

    print(ans)

if __name__ == '__main__':
    main()

