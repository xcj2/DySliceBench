# import sys
# input = sys.stdin.readline
import itertools

# 持っているビスケットを叩き、1枚増やす
# ビスケット A枚を 1円に交換する
# 1円をビスケット B枚に交換する
def main():
    n, k = input_list()
    a = input_list()
    d = {1: 0}
    pre = 1
    loop_start = 0
    loop_end = 0
    loop_pos = 0
    for i in range(1, n+1):
        new = a[pre-1]
        if d.get(new):
            loop_start = d[new]
            loop_end = i
            loop_pos = new
            break
        if i == k:
            print(new)
            exit()
        d[new] = i
        pre = new

    k -= loop_start
    k %= loop_end - loop_start
    pre = loop_pos
    for i in range(k):
        pre = a[pre-1]
    print(pre)

def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


if __name__ == "__main__":
    main()
