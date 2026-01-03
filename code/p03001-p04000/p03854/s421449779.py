import sys

# sys.stdin = open('c1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_str_list():
    return input().split()


def read_int():
    return int(input())


def read_str():
    return input()


def solve(s):
    words = ['dream', 'dreamer', 'erase', 'eraser']
    n = len(s)
    m = n
    while m > 0:
        found = False
        for w in words:
            stop = m
            start = m - len(w)
            if start >= 0:
                if s[start:stop] == w:
                    m = start
                    found = True
                    break
        if not found:
            return False
    return True


def main():
    s = read_str()
    res = solve(s)
    if res:
        print('YES')
    else:
        print('NO')


main()
