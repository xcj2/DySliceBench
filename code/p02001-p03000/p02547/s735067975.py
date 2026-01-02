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
    cnt = 0
    ans = 0
    for _ in range(n):
        a, b = input_int_list()
        if a == b:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    else:
        ans = max(ans, cnt)

    if ans >= 3:
        print("Yes")
    else:
        print("No")
    return


if __name__ == "__main__":
    main()
