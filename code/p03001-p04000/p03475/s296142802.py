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
    times = []
    for _ in range(n - 1):
        times.append(input_int_list())

    for i in range(n - 1):
        cur = 0
        for j in range(i, n - 1):
            c, s, f = times[j]
            # 次の電車の出発時間を探索する
            time = s
            while time < cur:
                time += f
            cur = time + c
        print(cur)
    # はじめからゴールにいるケースを出力
    print(0)
    return


if __name__ == "__main__":
    main()
