# coding: utf-8
# Your code here!
# 幅優先探索（行きがけ）

import sys


def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    N, K = LI()
    Aarray = LI()

    # start = 1
    # for i in range(K):
    #     start *= Aarray[i]

    # for i in range(K, N):
    #     now = start/Aarray[i-K]*Aarray[i]
    #     if now > start:
    #         print("Yes")
    #     else:
    #         print("No")
    #     start = now

    for i in range(K, N):
        now = Aarray[i-K]
        now2 = Aarray[i]
        if now2 > now:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    main()
