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
    h, w, n = intin()
    init_pos_h, init_pos_w = intin()
    s = input()
    t = input()

    pos_h = init_pos_h
    pos_w = init_pos_w
    for i in range(n):
        if s[i] == 'L':
            pos_w -= 1
        if pos_w <= 0:
            print('NO')
            return
        if t[i] == 'R' and pos_w < w:
            pos_w += 1

    pos_h = init_pos_h
    pos_w = init_pos_w
    for i in range(n):
        #print('== %d' % pos_w)
        if s[i] == 'R':
            pos_w += 1
        #print('===== %d' % pos_w)
        if pos_w > w:
            print('NO')
            return
        if t[i] == 'L' and pos_w > 1:
            pos_w -= 1

    pos_h = init_pos_h
    pos_w = init_pos_w
    for i in range(n):
        if s[i] == 'U':
            pos_h -= 1
        if pos_h <= 0:
            print('NO')
            return
        if t[i] == 'D' and pos_h < h:
            pos_h += 1

    pos_h = init_pos_h
    pos_w = init_pos_w
    for i in range(n):
        if s[i] == 'D':
            pos_h += 1
        if pos_h > h:
            print('NO')
            return
        if t[i] == 'U' and pos_h > 1:
            pos_h -= 1

    print('YES')


if __name__ == '__main__':
    main()
