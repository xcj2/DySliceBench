import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n = input_int()
    x_cur, y_cur, t_cur = 0, 0, 0
    for _ in range(n):
        t, x, y = input_int_list()
        dx = abs(x - x_cur)
        dy = abs(y - y_cur)
        dt = t - t_cur
        if dx + dy > dt:
            print("No")
            return
        if dt % 2 != (dx + dy) % 2:
            print("No")
            return
        else:
            x_cur, y_cur, t_cur = x, y, t
    print("Yes")
    return


if __name__ == "__main__":
    main()
