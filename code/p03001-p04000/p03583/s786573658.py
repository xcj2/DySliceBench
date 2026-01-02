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
    for a in range(1, 3501):
        for b in range(1, 3501):
            if 4 * a * b - n * b - n * a == 0:
                continue
            c = (n * a * b) // (4 * a * b - n * b - n * a)
            if c < 1:
                continue
            if 4 * a * b * c == n * (a * b + b * c + c * a):
                print(a, b, c)
                return
    return


if __name__ == "__main__":
    main()
