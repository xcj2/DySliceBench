import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

from itertools import accumulate

n,k = readints()
a = readints()

for _ in range(k):
    b = [0]*(n+1)
    for i in range(n):
        b[max(0,i-a[i])]+=1
        b[min(n,i+a[i]+1)]-=1
    a = list(accumulate(b))[:-1]
    if min(a)==n:
        break
printline(a)






