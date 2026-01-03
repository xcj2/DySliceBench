#!/usr/bin/env python3


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [tuple(map(typ, input().split())) if m > 1 else typ(input()) for _ in range(n)]


def main():
    W, H, N = read_h()
    pts = read_v(N, m=3)
    area = [[0, 0], [W, H]]

    for x, y, a in pts:
        if a == 1 and area[0][0] < x:
            area[0][0] = x
        elif a == 2 and area[1][0] > x:
            area[1][0] = x
        elif a == 3 and area[0][1] < y:
            area[0][1] = y
        elif a == 4 and area[1][1] > y:
            area[1][1] = y

        if area[1][0] - area[0][0] <= 0 or area[1][1] - area[0][1] <= 0:
            print(0)
            return

    ans = (area[1][0] - area[0][0]) * (area[1][1] - area[0][1])
    print(ans)


if __name__ == '__main__':
    main()
