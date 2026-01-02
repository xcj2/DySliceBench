#!/usr/bin/env python3
import collections as cl
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def battle(enemy, r, s, p):
    if enemy == "r":
        return p
    if enemy == "s":
        return r
    if enemy == "p":
        return s


def main():
    N, K = MI()
    r, s, p = MI()
    t = input()
    splited_t = [[] for i in range(K)]

    for i in range(N):
        amari = i % K
        splited_t[amari].append(t[i])

    ans = 0
    for i in range(K):
        targets = splited_t[i]
        score = battle(targets[0], r, s, p)
        ans += score
        won = True
        for j in range(1, len(targets)):
            if targets[j] == targets[j - 1] and won:
                won = False
                continue
            score = battle(targets[j], r, s, p)
            won = True
            ans += score
    print(ans)


main()
