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

def solve():
    [D, T, S] = inlt()
    return "Yes" if T * S >= D else "No" 
    

if len(sys.argv) > 1 and sys.argv[1].startswith("input"):
    f = open("./" + sys.argv[1], 'r')
    input = f.readline

res = solve()
print(str(res))
