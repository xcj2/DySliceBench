import collections


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def gcd(a, b):
    if a > b:
        a, b = (b, a)
    while b:
        a, b = b, a % b
    return a


def main():
    a, b = map(int, input().split())
    gcd_num = gcd(a, b)
    c = collections.Counter(prime_factorize(gcd_num))
    # print(prime_factorize(gcd_num))
    # cには１が含まれていないので、その分カウントを増やす
    print(len(c) + 1)


if __name__ == '__main__':
    main()
