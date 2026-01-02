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
x, y, z=mi()
for _ in range(n-1):
    a, b, c=mi()
    a+=max(y, z)
    b+=max(x, z)
    c+=max(y, x)
    x, y, z=a, b, c
print(max(x, y, z))