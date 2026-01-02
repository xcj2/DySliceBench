
import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))


n,k = readints()
a = readints()

l = 0
r = 10**10

while r-l>1:
    m = (l+r)//2
    x = [(a[i]-1)//m for i in range(n)]
    if sum(x)<=k:
        r = m
    else:
        l = m

print(r)
