# import sys
# input = sys.stdin.readline
import itertools


# 持っているビスケットを叩き、1枚増やす
# ビスケット A枚を 1円に交換する
# 1円をビスケット B枚に交換する
def main():
    n, m = input_list()
    balls = [1] * n
    reds = [False] * n
    reds[0] = True
    for _ in range(m):
        x, y = input_list()
        if reds[x-1]:
            reds[y-1] = True
        balls[x-1] -= 1
        balls[y-1] += 1
        if balls[x-1] == 0:
            reds[x-1] = False
    c = 0
    for v in reds:
        if v:
            c += 1
    print(c)


def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


if __name__ == "__main__":
    main()
