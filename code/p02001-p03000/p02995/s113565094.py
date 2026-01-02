

def read_input():
    a, b, c, d = map(int, input().split())

    return a, b, c, d

# baseの倍数がfrom_n ~ to_nにいくつあるか数える
def count_multiples(from_n, to_n, base):
    # from_nより大きい最小の倍数
    if from_n % base == 0:
        a = from_n // base
    else:
        a = from_n // base + 1
    left = a

    # to_nより小さい最大の倍数
    a = to_n // base
    right = a

    if left > right:
        return 0

    return right - left + 1

def euclidian(c, d):
    if c > d:
        p = c
        q = d
    else:
        p = d
        q = c

    while q:
        r = p % q
        p = q
        q = r

    return p


def submit():
    a, b, c, d = read_input()

    all_n = b - a + 1

    # cで割り切れる数
    c_div = count_multiples(a, b, c)

    # dで割り切れる数
    d_div = count_multiples(a, b, d)

    # cdの最小公倍数で割り切れる数
    min_mul = c * d // euclidian(c, d)
    cd_div = count_multiples(a, b, min_mul)


    print(all_n - c_div - d_div + cd_div)


if __name__ == '__main__':
    submit()
