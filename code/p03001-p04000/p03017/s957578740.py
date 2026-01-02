import os
import sys

if os.getenv('LOCAL'):
    sys.stdin = open('_in.txt', 'r')

sys.setrecursionlimit(2147483647)
INF = float('inf')

N, A, B, C, D = list(map(int, sys.stdin.readline().split()))
S = '.' + sys.stdin.readline().rstrip()


def can_go(s, e):
    i = s + 1
    while i <= e:
        if S[i - 1] == S[i] == '#':
            return False
        i += 1
    return True


def solve2():
    assert D < C
    if not can_go(A, C) or not can_go(B, D):
        return False
    i = B
    while i <= D:
        if S[i - 1] == S[i] == S[i + 1] == '.':
            return True
        i+=1
    return False


def solve():
    if C < D:
        return can_go(A, D)
    return solve2()


if solve():
    print('Yes')
else:
    print('No')
