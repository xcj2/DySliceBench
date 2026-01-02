import bisect
import sys
import math
input = sys.stdin.readline
import functools

from collections import defaultdict

############ ---- Input Functions ---- ############

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

############ ---- Solution ---- ############

def diff(S, i, T):
    res = 0
    for j in range(len(T)):
        if S[i + j] != T[j]:
            res += 1
    return res

def solve():
    S = input().rstrip()
    T = input().rstrip()
    res = 10 ** 9
    for i in range(0, len(S)):
        if i + len(T) - 1 >= len(S):
            continue
        res = min(res, diff(S, i, T))
    return res

    

if len(sys.argv) > 1 and sys.argv[1].startswith("input"):
    f = open("./" + sys.argv[1], 'r')
    input = f.readline

res = solve()
print(str(res))
