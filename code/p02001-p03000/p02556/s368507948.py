import math
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
    _x = []
    _y = []
    for _ in range(n):
        x, y = input_int_list()
		# 座標系を45度回転させて考える
        _x.append(x - y)
        _y.append(x + y)
	
    ans = max(max(_x) - min(_x), max(_y) - min(_y))

    print(ans)
    return


if __name__ == "__main__":
    main()
