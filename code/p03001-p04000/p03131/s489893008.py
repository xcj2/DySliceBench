import sys
input = sys.stdin.readline
import math


# 持っているビスケットを叩き、1枚増やす
# ビスケット A枚を 1円に交換する
# 1円をビスケット B枚に交換する
def main():
    k, a, b = input_list()
    # 交換レートが同じなら叩き続けたほうがいい 交換には手数２回消費つまりA + 3 <= B
    if b-a <= 2:
        print(k+1)
    else:
        bis = a
        k -= a-1
        if k % 2 == 1:
            bis += 1
            k -= 1
        bis += (b-a)*(k//2)
        print(bis)


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)


def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


if __name__ == "__main__":
    main()
