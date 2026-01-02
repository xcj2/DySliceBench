from math import *
import sys,bisect,copyreg,copy,statistics,os
def inp(): return sys.stdin.readline().strip()
def IIX(): return (int(x) for x in sys.stdin.readline().split())
def II(): return (int(inp()))
def LI(): return list(map(int, inp().split()))
def LS(): return list(map(str, inp().split()))
def L(x):return list(x)
def out(var): return sys.stdout.write(str(var))
def binary_search(arr, x): 
    left = 0
    right = len(arr) - 1
    mid = 0
    while left <= right:   
        mid = (left + left) // 2
        if arr[mid] < x: 
            left = mid + 1
        elif arr[mid] > x: 
            right = mid - 1
        else: 
            return mid
    return -1

s=inp()
c=0
if s.count("R")==1:
    out(1)
else:
    for i in range(3):
        if s[i]=='R':
            c+=1
        elif s[i]=='S' and i!=2:
            c= 0
    out(c)














 








