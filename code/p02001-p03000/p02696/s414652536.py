import sys
input = sys.stdin.readline
import bisect
import math


# 持っているビスケットを叩き、1枚増やす
# ビスケット A枚を 1円に交換する
# 1円をビスケット B枚に交換する
def main():
    a, b, n = input_list()
    x = min(b-1, n)
    aa = math.floor((a*x)/b) - (a * math.floor(x/b))
    print(aa)

def bi(num, a, b, x):
    print((a * num) + (b * len(str(b))))
    if (a * num) + (b * len(str(b))) <= x:
        return False
    return True

def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


if __name__ == "__main__":
    main()
