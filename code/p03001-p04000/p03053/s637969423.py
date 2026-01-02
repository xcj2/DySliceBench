###############################################################################

from bisect import bisect_left as binl
from copy import copy

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


def safe_ref(listlist, x, y):
    if x < 0 or y < 0 or x >= len(listlist) or y >= len(listlist[0]):
        return None
    try:
        return listlist[x][y]
    except:
        return None

def main():
    h, w = intin()
    alistlist = []
    for i in range(h):
        alistlist.append([s for s in input()])

    count = 0
    check_list = []

    for i, alist in enumerate(alistlist):
        for j, a in enumerate(alist):
            if a == '#':
                count += 1
                check_list.append((i, j))

    for repeated in range(h * w * 3):
        if count == h * w:
            print(repeated)
            return

        new_alistlist = copy(alistlist)
        next_list = []

        for i, j in check_list:
            if safe_ref(alistlist, i+1, j) == '.':
                new_alistlist[i+1][j] = '#'
                next_list.append((i+1, j))
                count += 1
            if safe_ref(alistlist, i-1, j) == '.':
                new_alistlist[i-1][j] = '#'
                next_list.append((i-1, j))
                count += 1
            if safe_ref(alistlist, i, j+1) == '.':
                new_alistlist[i][j+1] = '#'
                next_list.append((i, j+1))
                count += 1
            if safe_ref(alistlist, i, j-1) == '.':
                new_alistlist[i][j-1] = '#'
                next_list.append((i, j-1))
                count += 1

        check_list = next_list
        alistlist = new_alistlist


if __name__ == '__main__':
    main()
