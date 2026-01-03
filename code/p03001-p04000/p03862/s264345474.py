import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    # 入力
    n, x = input_int_list()
    A = [0] + input_int_list() + [0]
    ans = 0
    # 方針
    # 貪欲にi+1を減らしていく
    for i in range(n + 1):
        if A[i] + A[i + 1] > x:
            dif = min(A[i + 1], A[i] + A[i + 1] - x)
            ans += dif
            A[i + 1] -= dif

    print(ans)
    return


if __name__ == "__main__":
    main()
