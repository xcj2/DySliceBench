#!/usr/bin/env python3
import sys


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    N = II()
    ac = 0
    wa = 0
    tle = 0
    re = 0
    for i in range(N):
        target = input()
        if target == "AC":
            ac += 1
        if target == "WA":
            wa += 1
        if target == "TLE":
            tle += 1
        if target == "RE":
            re += 1
    print("AC x "+str(ac))
    print("WA x "+str(wa))
    print("TLE x "+str(tle))
    print("RE x "+str(re))


# oj t -c "pypy3 main.py"
# acc s main.py -- --guess-python-interpreter pypy
main()
