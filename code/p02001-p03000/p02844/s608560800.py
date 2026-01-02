import sys
from itertools import combinations

input = sys.stdin.readline


def check_num(text):
    cnt = 0
    for i in range(10):
        index = text.find(str(i))
        if index != -1:
            cnt += 1
    return cnt


def main():
    # 種類
    # N = int(input())
    # S = input().strip()
    S = sum(str(i) for i in range(10))
    for i in range(10):
        index = S.find(str(i))
        if index != -1:
            a = check_num(S[index:])
    # 10個の数字
    # 最大1000件
    # 0-9:0-9:0-9
    # print(len(set(combinations(S, 3))))


def hoge():
    N = int(input())
    S = input().strip()
    count = 0
    for x in range(10):
        xindex = S.find(str(x))
        if xindex == -1:
            continue
        for y in range(10):
            yindex = S[xindex + 1 :].find(str(y))
            if yindex == -1:
                continue
            for z in range(10):
                zindex = S[xindex + 1 :][yindex + 1 :].find(str(z))
                if zindex == -1:
                    continue
                count += 1
    print(count)


if __name__ == "__main__":
    hoge()
