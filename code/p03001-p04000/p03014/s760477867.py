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
    num_tate = [[0 for j in range(W)] for i in range(H)]
    num_sum = [[0 for j in range(W)] for i in range(H)]
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
            if target[i] == "#":
                num_tate[i][j] == 0
                tmp += 1
            else:
                num_tate[i][j] = splited[tmp]

            num_sum[i][j] = num_tate[i][j] + num_yoko[i][j] - 1
            ans = max(ans, num_sum[i][j])
    print(ans)


main()
