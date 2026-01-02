
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

n = readint()
a = readints()

flag = 0

node = [1]
for i in range(n):
    if a[i]>node[-1]:
        flag = 1
        break
    else:
        node.append((node[-1]-a[i])*2)

if a[-1]>node[-1]:
    flag = 1

if flag:
    print(-1)
    exit()

node[n] = a[n]

for i in range(n-1,-1,-1):
    if node[i]>a[i]+node[i+1]:
        node[i] = a[i] + node[i+1]
    else:
        break
print(sum(node))