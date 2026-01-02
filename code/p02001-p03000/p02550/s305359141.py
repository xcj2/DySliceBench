#!/usr/bin/env python3
import sys
import collections as cl


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    N, X, M = MI()
    rep = []
    rep_set = set([])
    i = 1

    rep.append(X)
    rep_set.add(X)
    flag = True

    while flag and i < N:
        x = rep[i-1] ** 2 % M
        if x in rep_set:
            rep.append(x)
            break
        rep.append(x)
        rep_set.add(x)
        i += 1

    if i == N:
        print(sum(rep))
    else:
        l = rep.index(rep[-1])
        rep_leng = i - l
        rep_sum = sum(rep[l:i])
        ans = 0
        ans += sum(rep[:l])
        N -= l
        rep_num = N // rep_leng
        rep_amari = N % rep_leng
        ans += rep_sum * rep_num
        ans += sum(rep[l:l+rep_amari])
        print(ans)


main()
