#!/usr/bin/env python
# coding: utf-8

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

def calc(s, k):
    ret = 0
    rev = 0
    c = s[0]
    for i in range(1, len(s)):
        if s[i] == c:
            ret += 1
            continue
        rev += 1
        c = s[i]
    ret += min(rev, k*2)
    k -= rev//2
    return ret


def main():
    n, k = rli()
    s = input()
    rs = ""
    for i in range(len(s)):
        if (s[n-i-1] == 'L'): rs += 'R'
        else: rs += 'L'
    a1 = calc(s,k)
    a2 = calc(rs,k)
    # print(s)
    # print(rs)
    print(max(a1, a2))


if __name__ == '__main__':
    main()
