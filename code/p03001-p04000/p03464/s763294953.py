import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

import math

k = readint()
a = readints()

flag = 0
if a[-1]!=2:
    flag = 1

b = 2
c = 2
for i in range(k-1,0,-1):
    b = math.ceil(b/a[i-1]) * a[i-1]
    c = ((c+a[i]-1)//a[i-1]) * a[i-1]
    if c == 0:
        flag = 1
        break
    if b>c:
        flag = 1
        break

c = c+a[0]-1

if flag:
    print(-1)
else:
    print(b,c)




