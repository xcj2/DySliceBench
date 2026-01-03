import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    from collections import Counter
    n = input_int()
    A = input_int_list()
    A_cnt = Counter(A).most_common()
    A_cnt = [list(a) for a in A_cnt]
    cnt = 0
    for i in range(len(A_cnt)):
        if A_cnt[i][1] > 2:
            if A_cnt[i][1] % 2 == 1:
                cnt += A_cnt[i][1] // 2
                A_cnt[i][1] = 1
            elif A_cnt[i][1] % 2 == 0:
                cnt += (A_cnt[i][1] // 2) - 1
                A_cnt[i][1] = 2
        if A_cnt[i][1] == 2:
            if i + 1 < len(A_cnt):
                A_cnt[i + 1][1] -= 1
            A_cnt[i][1] = 1
            cnt += 1
    print(n - cnt * 2)
    return


if __name__ == "__main__":
    main()
