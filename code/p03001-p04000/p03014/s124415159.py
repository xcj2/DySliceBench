#!/usr/bin/env python3
import sys
import collections as cl


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    H, W = MI()
    room = [["" for j in range(W)] for i in range(H)]
    roomT = [["" for i in range(H)] for j in range(W)]
    num_yoko = [[0 for j in range(W)] for i in range(H)]
    for i in range(H):
        row = input()

        splited = list(map(len, row.split('#')))
        tmp = 0
        for j in range(W):
            roomT[j][i] = row[j]
            room[i][j] = row[j]
            if row[j] == "#":
                num_yoko[i][j] = 0
                tmp += 1
            else:
                num_yoko[i][j] = splited[tmp]

    ans = 0

    for j in range(W):
        target = roomT[j]
        splited = list(map(len, "".join(target).split('#')))
        tmp = 0
        for i in range(H):
            num_tate = 0 if target[i] == "#" else splited[tmp]
            ans = max(ans,  num_tate + num_yoko[i][j] - 1)
            if target[i] == "#":
                tmp += 1
    print(ans)


main()
