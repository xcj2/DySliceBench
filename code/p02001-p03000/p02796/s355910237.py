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
    arms = []
    # 区間スケジューリング
    for _ in range(n):
        x, l = input_int_list()
        arms.append((x - l, x + l))
    arms = sorted(arms, key=lambda x: x[1])
    prev_r = -float("inf")
    cnt = 0
    for left, right in arms:
        if prev_r > left:
            continue
        cnt += 1
        prev_r = right

    print(cnt)

    return


if __name__ == "__main__":
    main()
