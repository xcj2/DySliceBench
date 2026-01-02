#!/usr/bin/env python
# coding: utf-8

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

def check(s):
    for i in range(len(s)):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

def main():
    n, k, q = rli()
    solve = [0 for _ in range(n+1)]
    for i in range(q):
        a = ri()
        solve[a] += 1
    for i in range(n):
        if k-q+solve[i+1] > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()
