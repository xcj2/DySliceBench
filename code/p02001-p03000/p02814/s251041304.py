def count_power_of_2(x):
    cnt = 0
    while x % 2 == 0:
        x //= 2
        cnt += 1
    return cnt


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    N, M = map(int, input().split())
    a = map(int, input().split())
    *a, = map(lambda x: x >> 1, a)

    power = count_power_of_2(a[0])

    if any(count_power_of_2(x) != power for x in a):
        print(0)
        return

    common = 1 << power

    base = common
    for x in a:
        x //= common
        base = lcm(base, x)

    ret = (M // base) - (M // (base * 2))
    print(ret)
    return


if __name__ == '__main__':
    main()
