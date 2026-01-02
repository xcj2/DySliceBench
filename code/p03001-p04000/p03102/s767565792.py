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
    n, m, c = intin()
    blist = intina()
    alistlist = []
    for i in range(n):
        alistlist.append(intina())

    count = 0
    for alist in alistlist:
        csum = 0
        for i, a in enumerate(alist):
            csum += a * blist[i]
        csum += c
        if csum > 0:
            count += 1

    print(count)


if __name__ == '__main__':
    main()
