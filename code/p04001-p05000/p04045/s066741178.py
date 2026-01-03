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
    D = input_int_list()

    # N < 10000のため、嫌いな数字にかかわらず、
    # N <= ans < 100000の範囲に答えは収まる。
    # 計算量はO(n) (max_n = 5 * 10**4)

    for i in range(n, 100000):
        flag = True
        for j in str(i):
            if int(j) in D:
                flag = False
            if not flag:
                break
        if flag:
            print(i)
            return

    return


if __name__ == "__main__":
    main()
