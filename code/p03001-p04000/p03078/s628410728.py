###############################################################################

from bisect import bisect_left as binl

def intin():
    input_tuple = input().split()
    if len(input_tuple) <= 1:
        return int(input_tuple[0])
    return tuple(map(int, input_tuple))


def intina():
    return [int(i) for i in input().split()]


def intinl(count):
    return [intin() for _ in range(count)]


def modadd(x, y):
    global mod
    return (x + y) % mod


def modmlt(x, y):
    global mod
    return (x * sy) % mod


def lcm(x, y):
    while y != 0:
        z = x % y
        x = y
        y = z
    return x


###############################################################################


def main():
    x, y, z, k = intin()
    alist = intina()
    blist = intina()
    clist = intina()

    ablist = []
    for a in alist:
        for b in blist:
            ablist.append(a + b)

    ablist.sort(reverse=True)

    abclist = []
    for ab in ablist[:(k+1)]:
        for c in clist:
            abclist.append(ab + c)

    abclist.sort(reverse=True)

    for i in range(k):
        print(abclist[i])


if __name__ == '__main__':
    main()
