from math import sqrt, floor, log


def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, floor(num / 2) + 1):
        if i == num:
            break
        if num % i == 0:
            return False
    return True


def get_divisors3(num):
    ans = []
    value = num
    i = 2
    while (i * i) <= num:
        count = 0
        while value % i == 0:
            count += 1
            value = value // i

        if count != 0:
            ans.append((i, count))
        i += 1
    return ans


def main():
    n, p = [int(i) for i in input().split()]
    if n == 1:
        print(p)
    elif p == 1:
        print(1)
    else:
        ds = get_divisors3(p)
        ans = 1
        for d in ds:
            if d[1] >= n:
                ans *= d[0] ** (d[1] // n)
        print(int(ans))


if __name__ == '__main__':
    main()
