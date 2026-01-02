# -*- coding: utf-8 -*-
import math


def is_sosu(n):

    if n == 2:
        return True

    if n < 2 or n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


def similar_to_2017(n):
    if is_sosu(n) and is_sosu((n + 1) / 2):
        return True

    return False


def main():
    q = int(input())
    in_target = [tuple(map(int, input().split())) for i in range(q)]

    similar_to_2017s = {}
    for i in range(1, 100001, 2):
        if similar_to_2017(i):
            similar_to_2017s[i] = 1 + similar_to_2017s.get(i - 2, 0)
        else:
            similar_to_2017s[i] = similar_to_2017s.get(i - 2, 0)

    for target in in_target:
        cnt = similar_to_2017s.get(target[1], 0) - similar_to_2017s.get(target[0] - 2, 0)

        print(cnt)


if __name__ == '__main__':
    main()


