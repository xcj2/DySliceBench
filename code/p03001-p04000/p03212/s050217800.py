import math
import itertools


def solve():
    n = read()
    result = think(n)
    write(result)


def read():
    return read_int(1)[0]


def read_int(n):
    return list(map(int, input().rstrip().split()[:n]))


def think(n):
    if n < 357:
        return 0
    digits = math.ceil(math.log10(n))
    if digits % 10 == 0:
        digits += 1

    count = 0
    dictionary = ['3', '5', '7']
    for d in range(3, digits + 1):
        for list_of_012 in itertools.product([0, 1, 2], repeat=d):
            buf = ''
            for elem in list_of_012:
                buf += str(dictionary[elem])
            if int(buf) <= n and buf.count('3') >= 1 and buf.count('5') >= 1 and buf.count('7') >= 1:
                # print(buf)
                count += 1
    return count


def write(result):
    print(result)


if __name__ == '__main__':
    solve()