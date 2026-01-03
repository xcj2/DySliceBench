# import sys
# input = sys.stdin.readline
import itertools

# 持っているビスケットを叩き、1枚増やす
# ビスケット A枚を 1円に交換する
# 1円をビスケット B枚に交換する
def main():
    h, w = input_list()
    count = 0
    for _ in range(h):
        s = list(input())
        count += s.count('#')
    if h+w-1 == count:
        print('Possible')
    else:
        print('Impossible')

def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


if __name__ == "__main__":
    main()
