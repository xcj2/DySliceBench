import sys
input = sys.stdin.readline
import bisect


# 持っているビスケットを叩き、1枚増やす
# ビスケット A枚を 1円に交換する
# 1円をビスケット B枚に交換する
def main():
    n = int(input())
    l = sorted(input_list())
    ans = 0
    for a in range(n):
        for b in range(a+1, n):
            ans += bisect.bisect_left(l, l[a]+l[b]) - (b+1)
    print(ans)

def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


if __name__ == "__main__":
    main()
