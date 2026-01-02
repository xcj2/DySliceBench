import sys

input = lambda: sys.stdin.readline()


def cin_int_list():
    return [int(x) for x in input().split()]


def cin_int_iter():
    return (int(x) for x in input().split())


def cin_int():
    return int(input())


def cout_int_iter(a):
    print(' '.join(map(str, a)))


def iota(n, start=0):
    return list(range(start, n))


def cin_digits_list():
    return [ord(x) - ord('0') for x in input()]


def main():
    a, b, c, k = cin_int_iter()

    ret = 0

    ret += min(a, k)
    k -= min(a, k)

    if k == 0:
        print(ret)
        return

    k -= min(b, k)

    if k == 0:
        print(ret)
        return

    ret -= min(c, k)
    k -= min(c, k)

    print(ret)


main()
