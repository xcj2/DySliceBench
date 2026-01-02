import sys
import socket

if socket.gethostname() in ['N551J', 'F551C']:
    sys.stdin = open('e1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_int():
    return int(input())


def read_str_list():
    return input().split()


def read_str():
    return input()


def solve():
    s = list(map(int, read_str()))
    n = len(s)
    if s[0] != 1:
        return -1
    if s[n - 1] != 0:
        return -1
    for i in range(n - 1):
        if s[i] != s[n - 2 - i]:
            return -1
    x = [i for i in range(n) if s[i] == 1]
    k = len(x)
    body = list(range(1, k + 2))
    res = [[body[i], body[i + 1]] for i in range(k)]
    p = k + 2
    for j in range(1, k):
        for l in range(x[j] - x[j-1] - 1):
            edge = [body[j], p]
            p += 1
            res.append(edge)
    return res


def main():
    res = solve()
    if res == -1:
        print(res)
        return
    for edge in res:
        print(*edge)


if __name__ == '__main__':
    main()
