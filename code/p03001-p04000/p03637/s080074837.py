import sys
from collections import Counter

# sys.stdin = open('c1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_str_list():
    return input().split()


def read_int():
    return int(input())


def read_str():
    return input()


def solve():
    n = read_int()
    a = read_int_list()
    c = Counter()

    for x in a:
        if x % 2 == 1:
            c[0] += 1
        elif x % 4 == 2:
            c[1] += 1
        else:
            c[2] += 1

    if c[0] > c[2] + 1:
        return False
    if c[0] == c[2] + 1:
        return c[1] == 0
        # if c[1] == 0:
        #     return True
        # else:
        #     return False
    if c[0] <= c[2]:
        return True


def main():
    res = solve()
    if res:
        print('Yes')
    else:
        print('No')


main()
