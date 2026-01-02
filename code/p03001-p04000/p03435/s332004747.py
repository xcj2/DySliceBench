import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    c = []
    for _ in range(3):
        c.append(input_int_list())

    if (c[0][0] - c[1][0]) == (c[0][1] - c[1][1]) and (c[0][1] - c[1][1]) == (c[0][2] - c[1][2]) and (c[0][0] - c[2][0]) == (c[0][1] - c[2][1]) and (c[0][1] - c[2][1]) == (c[0][2] - c[2][2]) and (c[2][0] - c[1][0]) == (c[2][1] - c[1][1]) and (c[2][1] - c[1][1]) == (c[2][2] - c[1][2]):
        print("Yes")
    else:
        print("No")

    return


if __name__ == "__main__":
    main()
