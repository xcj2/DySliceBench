from sys import stdin
#from collections import deque
#from math import sqrt, floor, ceil, log, log2, log10, pi, gcd, sin, cos, asin
def ii(): return int(stdin.readline())
def fi(): return float(stdin.readline())
def mi(): return map(int, stdin.readline().split())
def fmi(): return map(float, stdin.readline().split())
def li(): return list(mi())
def lsi():
    x=list(stdin.readline())
    x.pop()
    return x
def si(): return stdin.readline()
############# CODE STARTS HERE #############
n=ii()
s=[0]*n
a=li()
s[n-2]=abs(a[n-2]-a[n-1])
for i in range(n-3, -1, -1):
    s[i]=min(abs(a[i]-a[i+1])+s[i+1], abs(a[i]-a[i+2])+s[i+2])
print(s[0])