import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    from collections import defaultdict
    n = input_int()
    A = input_int_list()
    cusum = [0] * (n + 1)
    # 累積和をとり、それぞれの現れる合計値の回数をとる
    cnt = defaultdict(int)
    cnt[0] += 1
    for i in range(1, n + 1):
        cusum[i] = cusum[i - 1] + A[i - 1]
        cnt[cusum[i]] += 1
    # 合計値が同じになる２箇所を選ぶと総和が0になる
    # その組み合わせを数え上げる。
    ans = 0
    for _, v in cnt.items():
        if v > 1:
            ans += (v * (v - 1)) // 2
    print(ans)

    return


if __name__ == "__main__":
    main()
