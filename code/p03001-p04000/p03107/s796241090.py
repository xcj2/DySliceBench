#!/usr/bin/python3
# ABC120: C
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def debug(*args): print("DEBUG:\t", *args, file=sys.stderr)


def combine(S, i):
    if S[i] != S[i+1]:
        S
        return S[0:i] + S[i+2:]
    else:
        assert False

def main(S, answer=0, _d=False):
    S = [int(x) for x in S]
    return solve(S, answer, _d)

def solve(S, answer=0, _d=False):
    i = 0
    while i < len(S) - 1:
        #debug(S, "i=%d"% i, answer)
        if S[i] != S[i+1]:
            answer += 2
            del S[i:i+2]
            i = max(i - 1, 0)
        else:
            i += 1
    debug("answer", answer)
    return answer

def check(S, expected):
    a = main(S)
    if a != expected:
        print(a)
        print("expected %d" % expected, "but %d" % a, "for", S)

if 1==0:
    check("0011", 4)
    check("101", 2)
    check("111", 0)
    check("010", 1)
    check("0", 0)
    check("11011010001011", 12)

print(main(input().strip()))
