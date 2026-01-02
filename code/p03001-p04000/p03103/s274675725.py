###############################################################################

from bisect import bisect_left as binl

def intin():
    input_tuple = input().split()
    if len(input_tuple) <= 1:
        return int(input_tuple[0])
    return map(int, input_tuple)


def intina():
    return [int(i) for i in input().split()]


def intinl(count):
    return [intin() for _ in range(count)]


def lcm(x, y):
    while y != 0:
        z = x % y
        x = y
        y = z
    return x


###############################################################################


def main():
    n, m = intin()
    ablist = intinl(n)
    ablist = [(a, b) for a, b in ablist]

    ablist.sort()

    count = 0
    yen = 0
    for a, b in ablist:
        if count + b >= m:
            yen += a * (m - count)
            count = m
            break
        yen += a * b
        count += b

    print(yen)


if __name__ == '__main__':
    main()
