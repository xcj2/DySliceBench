import sys
from collections import Counter

# sys.stdin = open('c1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_int():
    return int(input())


def read_str_list():
    return input().split()


def read_str():
    return input()


def solve():

    c = Counter()
    n = read_int()
    a = read_int_list()
    for x in a:
        if x % 2 == 1:
            c[0] += 1
        elif x % 4 == 2:
            c[1] += 1
        else:
            c[2] += 1
    if c[0] > c[2] + 1:
        return 'No'
    elif c[0] == c[2] + 1:
        if c[1] > 0:
            return 'No'
        else:
            return 'Yes'
    else:
        return 'Yes'


def main():
    res = solve()
    print(res)


if __name__ == '__main__':
    main()
