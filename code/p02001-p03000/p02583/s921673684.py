from math import *
import sys,bisect,copyreg,copy,statistics,os
def inp(): return sys.stdin.readline().strip()
def IIX(): return (int(x) for x in sys.stdin.readline().split())
def II(): return (int(inp()))
def LI(): return list(map(int, inp().split()))
def LS(): return list(map(str, inp().split()))
def L(x):return list(x)
def out(var): return sys.stdout.write(str(var))


n=II()
sizes=LI()
t=0
sizes.sort()

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if sizes[i] + sizes[j]> sizes[k] and sizes[i]!=sizes[j] and sizes[j]!=sizes[k]:
                t+=1

out(t)

















 








