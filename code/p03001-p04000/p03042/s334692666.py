#!/usr/bin/env python
# coding: utf-8

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

def isMM(s2):
    d = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    return s2 in d

def main():
    s = input()
    if isMM(s[0:2]):
        if isMM(s[2:]):
            print("AMBIGUOUS")
        else:
            print("MMYY")
    else:
        if isMM(s[2:]):
            print("YYMM")
        else:
            print("NA")


if __name__ == '__main__':
    main()
