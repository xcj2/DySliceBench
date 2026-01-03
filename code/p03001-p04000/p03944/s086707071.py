# import sys
# input = sys.stdin.readline
import itertools


# 持っているビスケットを叩き、1枚増やす
# ビスケット A枚を 1円に交換する
# 1円をビスケット B枚に交換する
def main():
    w, h, n = input_list()
    zahyou = [[0]*w for _ in range(h)]
    for _ in range(n):
        x, y, a = input_list()
        umeru(zahyou, x, y, a)
    ans = 0
    for hz in zahyou:
        ans += hz.count(0)
    print(ans)

def umeru(zu, x, y, a):
    for Y, row in enumerate(zu):
        for X, v in enumerate(row):
            if a == 1:
                if X < x:
                    zu[Y][X] = 1
            if a == 2:
                if X > x - 1:
                    zu[Y][X] = 1
            if a == 3:
                if Y < y:
                    zu[Y][X] = 1
            if a == 4:
                if Y > y - 1:
                    zu[Y][X] = 1


def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


if __name__ == "__main__":
    main()
