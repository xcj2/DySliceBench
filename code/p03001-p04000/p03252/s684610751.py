import sys
# sys.setrecursionlimit(100000)
from collections import Counter


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    S = input()
    T = input()
    S_cnt = Counter(S).most_common()
    T_cnt = Counter(T).most_common()
    if len(S_cnt) != len(T_cnt):
        print("No")
        return
    for i in range(len(S_cnt)):
        if S_cnt[i][1] == T_cnt[i][1]:
            continue
        else:
            print("No")
            return
    print("Yes")
    return


if __name__ == "__main__":
    main()
