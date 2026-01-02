#!/usr/bin/env python3
import sys
try: from typing import Any, Union, List, Tuple, Dict
except ImportError: pass
sys.setrecursionlimit(10**6)
def debug(*args): print(*args, file=sys.stderr)
def exit(): sys.exit(0)


N, M = map(int, input().split())
S = input()
T = input()


def gcd(a, b):
    # type: (int, int) -> int
    "最大公約数を計算する．0とか負の数が入るとヤバい"
    if b%a == 0:
        return a
    return gcd(b%a, a)


d = gcd(N, M)
n = N // d
m = M // d


for i in range(d):
    if S[i*n] != T[i*m]:
        print(-1)
        exit()
print(n*m*d)
