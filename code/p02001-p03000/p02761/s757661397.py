#!/usr/bin/env python
# coding: utf-8

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

def main():
    n, m = rli()
    digits = [-1 for _ in range(n)]
    for i in range(m):
        s, c = rli()
        s -= 1
        if digits[s] != -1 and digits[s] != c:
            print(-1)
            return
        digits[s] = c
    if n == 1:
        if digits[0] == -1:
            print(0)
        else:
            print(digits[0])
        return
    if digits[0] == 0:
        print(-1)
        return
    elif digits[0] == -1:
        digits[0] = 1
    for i in range(n):
        if digits[i] == -1:
            digits[i] = 0
    print("".join(map(str, digits)))
    


if __name__ == '__main__':
    main()
