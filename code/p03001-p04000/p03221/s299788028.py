import sys,collections,math;sys.setrecursionlimit(10**7)
from operator import itemgetter;
def Is(): return [int(x) for x in sys.stdin.readline().split()]
def Ss(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N,M = Is()
lis = []
for i in range(M):
    lis.append([i]+Is())
t = sorted(lis,key=itemgetter(1,2))
x,p = 0,1
for i in range(M):
    if p == t[i][1]:
        x += 1
        t[i] += [p,x]
    else:
        p = t[i][1]
        x = 1
        t[i] += [p,x]
t = sorted(t,key=itemgetter(0))
for e in t:
    print( (6-len(str(e[3])))*"0" + str(e[3]) + (6-len(str(e[4])))*"0" + str(e[4]))