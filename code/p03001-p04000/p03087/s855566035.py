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
    n, q = intin()
    s = input()
    lrlist = intinl(q)
    lrlist = [(l, r) for l, r in lrlist]

    prev = None
    pos_i_list = []
    for i, c in enumerate(s):
        if prev == 'A' and c == 'C':
            pos_i_list.append(i)
        prev = c

    for l, r in lrlist:
        start = binl(pos_i_list, l)
        end = binl(pos_i_list, r)
        print(end - start)


if __name__ == '__main__':
    main()
