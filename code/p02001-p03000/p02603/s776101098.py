import sys
import copy
def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
INF = 1000000000000

n = I()
a = LI()

m = 1000
c = 0
i = 0
while(i < n-1):
    if(c == 0):
        if(a[i] < a[i+1]):
            c = m // a[i]
            m = m % a[i]
    else:
        if(a[i] > a[i+1]):
            m = m + c * a[i]
            c = 0
    i = i+1

if(c != 0):
    m = m + c * a[n-1]

print(m)