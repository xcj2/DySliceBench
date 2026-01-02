#!/usr/bin/env python
# coding: utf-8

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

MOD = 10**9+7

def main():
    n, k = rli()
    la = rli()
    rev1 = 0
    rev2 = 0
    for i in range(len(la)):
        for j in range(len(la)):
            if la[i] > la[j]:
                if i < j:
                    rev1 += 1
                else:
                    rev2 += 1
    ans = rev1 * k*(k+1)//2 + rev2 * (k-1)*k//2
    ans %= MOD
    print(ans)


if __name__ == '__main__':
    main()
