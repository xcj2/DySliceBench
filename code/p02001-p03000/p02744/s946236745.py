#!/usr/bin/env python
# coding: utf-8

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

words = set()
alp = list("abcdefghij")
def dfs(n, s):
    if len(s) == n:
        return
    for i in range(0, len(s)):
        for c in alp:
            if ord(c)>ord(s[i])+1:
                break
            ns = s[:i+1]+c+s[i+1:]
            if ns in words:
                continue
            words.add(ns)
            dfs(n, ns)

def main():
    n = ri()
    if n == 1:
        print("a")
        return
    dfs(n, 'a')
    for w in sorted(words):
        if len(w) == n:
            print(w)



if __name__ == '__main__':
    main()
