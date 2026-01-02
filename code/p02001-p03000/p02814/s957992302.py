from functools import reduce


def count_factors(a, factor):
    count = 0
    while a % factor == 0:
        count += 1
        a //= factor
    return count


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(set(map(lambda x: int(x) // 2, input().split())))
    num_of_two = count_factors(a[0], 2)
    for ai in a[1:]:
        if count_factors(ai, 2) != num_of_two:
            print(0)
            exit()

    a_lcm = reduce(lambda x, y: lcm(x, y), a)
    if a_lcm > m:
        print(0)
        exit()

    print((m // a_lcm + 1) // 2)
