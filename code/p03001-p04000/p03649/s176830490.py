import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

from math import ceil

n = readint()
a = readints()

ans = 0
for i in range(n):
    a.sort()
    if a[-1]<n:
        break
    ans += 1
    for j in range(n-1):
        a[j]+=1
    a[-1]-=n

a.sort()
while a[-1]-a[0]>n+1:
    x = ceil((a[-1]-a[0]-n-1)/(n+1))
    ans += x
    for j in range(n-1):
        a[j] += x
    a[-1] -= n*x
    a.sort()
if a[-1]>n:
    ans += (a[0]-n+1)*n
    A = a[0]
    for i in range(n):
        a[i] -= A-n+1

while a[-1]>=n:
    ans += 1
    for j in range(n-1):
        a[j]+=1
    a[-1]-=n
    a.sort()

print(ans)


