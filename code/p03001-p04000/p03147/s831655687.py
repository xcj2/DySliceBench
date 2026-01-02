
import sys

input = sys.stdin.readline

# input = sys.stdin.readline
sys.setrecursionlimit(2147483647)


def split(h):
    pieces = []
    tmp = []
    for i in range(len(h)):
        if h[i] == 0:
            pieces.append(tmp)
            tmp = []
        else:
            tmp.append(h[i])

    pieces.append(tmp)
    return pieces


def f(h):
    if len(h) == 0:
        return 0

    ith = 0
    while True:
        maxh = max(h)
        if maxh == 0:
            break
        for i in range(len(h)):
            h[i] += 1
        ith += 1

    pieces = split(h)

    m = 0
    for piece in pieces:
        m += f(piece)

    return ith + m


def main():
    N = int(input())
    h = list(map(int, input().split()))
    h = [-i for i in h]

    pieces = split(h)

    m = 0
    for piece in pieces:
        m += f(piece)

    print(m)


if __name__ == '__main__':
    main()
