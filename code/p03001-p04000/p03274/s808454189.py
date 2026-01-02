import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n, k = input_int_list()
    X = input_int_list()
    ans = float("inf")
    for i in range(0, n - k + 1):
        tmp_min = X[i]
        tmp_max = X[i + k - 1]
        if tmp_max <= 0:
            tmp = abs(tmp_min)
        elif tmp_min >= 0:
            tmp = abs(tmp_max)
        else:
            tmp = min(abs(tmp_max), abs(tmp_min)) * 2 + max(abs(tmp_max), abs(tmp_min))
        ans = min(tmp, ans)
    print(ans)
    return


if __name__ == "__main__":
    main()
