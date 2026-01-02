def trial_division(n):
    a = [1]
    while n % 2 == 0:
        a.append(2)
        n /= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n /= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def gcd(x, y):
    if x > y:
        return gcd(y, x)
    # x <= y
    temp = y % x
    if temp == 0:
        return x
    else:
        return gcd(temp, x)


def main():
    a, b = map(int, input().split())
    gcd_ab = gcd(a, b)
    temp_list = trial_division(gcd_ab)
    # print(gcd_ab)
    # print(temp_list)
    temp_set = set(temp_list)
    print(len(temp_set))


if __name__ == '__main__':
    main()
    