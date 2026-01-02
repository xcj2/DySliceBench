import sys
import socket
from collections import deque


if socket.gethostname() in ['N551J', 'F551C']:
    in_file = 'f1.in'
    in_file = 'after_contest_01.in'
    sys.stdin = open(in_file)


def read_int_list():
    return list(map(int, input().split()))


def read_int():
    return int(input())


def read_str_list():
    return input().split()


def read_str():
    return input()


def solve():
    n, d, a = read_int_list()
    pairs = [read_int_list() for _ in range(n)]
    pairs.sort()
    x, h = map(list, zip(*pairs))

    res = 0
    damage = 0
    q = deque()
    for i in range(n):
        # print(i, damage, file=sys.stderr)
        while len(q) > 0 and q[0][0] + d < x[i]:
            y, m = q.popleft()
            damage -= m * a
        if damage < h[i]:
            y = x[i] + d
            quotient, rest = divmod(h[i] - damage, a)
            m = quotient + (rest > 0)
            q.append((y, m))
            damage += m * a
            res += m

    return res



def main():
    res = solve()
    print(res)


if __name__ == '__main__':
    main()
