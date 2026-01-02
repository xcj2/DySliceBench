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
    ans = 0
    if k == 0:
        print(n * n)
        return
    #  bを固定し、aとしてあり得る範囲をO(1)で求める。

    for b in range(k + 1, n + 1):
        ans += (b - k) * (n // b)
        if n % b >= k:
            ans += n % b - (k - 1)

    print(ans)
    return


if __name__ == "__main__":
    main()
