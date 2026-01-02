#!/usr/bin/env python
# coding: utf-8

inf = 10**9+7
def ng(key, c=None):
    if c is None:
        return key == "agc" or key == "gac" or key == "acg"
    if key[0] == 'a' and key[1] == 'g' and c == 'c':
        "ag.c"
        return True
    if key[0] == 'a' and key[2] == 'g' and c == 'c':
        "a.gc"
        return True
    if key[1] == 'a' and key[2] == 'g' and c == 'c':
        "agc"
        return True
    if key[1] == 'g' and key[2] == 'a' and c == 'c':
        "gac"
        return True
    if key[1] == 'a' and key[2] == 'c' and c == 'g':
        "acg"
        return True
    return False


def init():
    ret = {}
    for c1 in list('acgt'):
        for c2 in list('acgt'):
            for c3 in list('acgt'):
                key = c1+c2+c3
                if ng(key):
                    continue
                ret[key] = 1
    return ret


def next(dp):
    ndp = {}
    for key in dp:
        for c in list('atcg'):
            if ng(key, c):
                continue
            nkey = key[1:] + c
            ndp.setdefault(nkey, 0)
            ndp[nkey] += dp[key] % inf
    return ndp


def main():
    N = int(input())
    dp = init()
    for i in range(N-3):
        dp = next(dp)
    print(sum(dp.values()) % inf)


if __name__ == '__main__':
    main()
