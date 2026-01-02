import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

from collections import Counter

n = readint()
a = sorted(readints())

c = Counter(a)
ans = 0
b = [1]*(max(c)+1)
l = max(c)

for x in c:
    if c[x]==1 and b[x]==1:
        ans += 1
    for i in range(1,l//x+1):
        b[x*i] = 0

print(ans)



