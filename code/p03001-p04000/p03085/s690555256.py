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
    b = input()

    if b == 'A':
        print('T')
    if b == 'T':
        print('A')
    if b == 'C':
        print('G')
    if b == 'G':
        print('C')


if __name__ == '__main__':
    main()
