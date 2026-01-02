#!/usr/bin/env python
# coding: utf-8

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

def mark(b, check, la):
    for i in range(3):
        for j in range(3):
            if la[i][j] == b:
                check[i][j] = True

def ok(check):
    for i in range(3):
        if check[i][0] and check[i][1] and check[i][2]:
            return True
        if check[0][i] and check[1][i] and check[2][i]:
            return True
    if check[0][0] and check[1][1] and check[2][2]:
        return True
    if check[2][0] and check[1][1] and check[0][2]:
        return True
    return False


def main():
    check = [[False for _ in range(3)] for _ in range(3)]
    la = []
    for i in range(3):
        l = rli()
        la.append(l)
    n = ri()
    for i in range(n):
        b = ri()
        mark(b, check, la)
    if ok(check):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
