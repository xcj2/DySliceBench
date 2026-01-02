def mpow(x, n):
    result = 1
    while n != 0:
        if n & 1 == 1:
            result *= x
            result %= 1000000007
        x *= x
        x %= 1000000007
        n >>= 1

    return result

def mcomb(n, k):
    a = 1
    b = 1
    for i in range(k):
        a *= n - i
        a %= 1000000007
        b *= i + 1
        b %= 1000000007

    return a * mpow(b, 1000000005) % 1000000007

def main():
    n, a, b = map(int, input().split())
    
    ans = mpow(2, n) - mcomb(n, a) - mcomb(n, b) - 1

    print(ans%1000000007)

if __name__ == '__main__':
    main()