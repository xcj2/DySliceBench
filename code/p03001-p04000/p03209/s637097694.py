import sys
# sys.setrecursionlimit(100000)
from functools import lru_cache


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n, x = input_int_list()
    layer_size = [1]
    p_cnt = [1]

    for _ in range(50):
        layer_size.append(layer_size[-1] * 2 + 3)
        p_cnt.append(p_cnt[-1] * 2 + 1)

    @lru_cache(None)
    def L(level, x):
        if x == 1:
            if level == 0:
                return 1
            else:
                return 0
        l = layer_size[level - 1]
        p = p_cnt[level - 1]
        if x <= l + 1:
            return L(level - 1, x - 1)
        elif x == l + 2:
            return p + 1
        elif x <= 2 + l * 2:
            return p + 1 + L(level - 1, x - l - 2)
        else:
            return 2 * p + 1
    print(L(n, x))
    return


if __name__ == "__main__":
    main()
