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
    dishes = []
    for i in range(n):
        a, b = input_int_list()
        dishes.append((a, b, a + b))
    # a+bの合計値でソートする
    dishes = sorted(dishes, key=lambda x: x[2])
    t_sum = 0
    a_sum = 0
    is_takahashi = True  # True => Tさんのターン
    while dishes:
        a, b, _ = dishes.pop()
        if is_takahashi:
            t_sum += a
        else:
            a_sum += b
        is_takahashi = not is_takahashi
    print(t_sum - a_sum)

    return


if __name__ == "__main__":
    main()
