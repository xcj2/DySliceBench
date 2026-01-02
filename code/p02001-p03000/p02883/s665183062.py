import sys
import math
import bisect
 
 
sys.setrecursionlimit(1000000000)
def input():
    return sys.stdin.readline().strip()
 
def iinput():
    return int(input())
 
def finput():
    return float(input())
 
def tinput():
    return input().split()
 
def rinput():
    return map(int, tinput())
 
def rlinput():
    return list(rinput())
 
def modst(a, s):
    res = 1
    while s:
        if s % 2:
            res *= a
        a *= a
        s //= 2
    return res

 
def main():
    n, k = rinput()
    a = sorted(rlinput())
    s = sorted(rlinput())
    l, res = -1, 10 ** 12
    while res - l > 1:
        m = (res + l) // 2
        q = k    
        for i in range(n):
            w = a[i] - (m // s[- i - 1])
            q -= max(0, w)
        if q < 0:
            l = m
        else:
            res = m
    print(res)        
main()