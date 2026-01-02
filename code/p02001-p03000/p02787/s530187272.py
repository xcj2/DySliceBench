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

inf = 10 ** 20

def solve():
    H, n = read_int_list()
    a, b = [0] * n, [0] * n
    for i in range(n):
        a[i], b[i] = read_int_list()
    cost = [0] * (H+1)
    for h in range(1, H+1):
        c = inf
        for i in range(n):
            health = h - a[i]
            if health < 0:
                health = 0
            if c > cost[health] + b[i]:
                c = cost[health] + b[i]
        cost[h] = c

    # for h in range(H + 1):
    #     print('\t', h, cost[h], file=sys.stderr)

    return cost[H]



def main():
    res = solve()
    print(res)


if __name__ == '__main__':
    main()
