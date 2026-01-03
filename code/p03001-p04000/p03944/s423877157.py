#!/usr/bin/env python3


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [tuple(map(typ, input().split())) if m > 1 else typ(input()) for _ in range(n)]


def main():
    W, H, N = read_h()
    pts = read_v(N, m=3)
    rec = [0, 0, W, H]

    for x, y, a in pts:
        if a == 1:
            rec[0] = max(rec[0], x)
        elif a == 2:
            rec[2] = min(rec[2], x)
        elif a == 3:
            rec[1] = max(rec[1], y)
        elif a == 4:
            rec[3] = min(rec[3], y)

        if rec[2] - rec[0] <= 0 or rec[3] - rec[1] <= 0:
            print(0)
            return

    ans = (rec[2] - rec[0]) * (rec[3] - rec[1])
    print(ans)


if __name__ == '__main__':
    main()
