import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

from operator import itemgetter

n = readint()
a = []
for i in range(n):
    x,l = readints()
    a.append([x-l,x+l])

a.sort(key = itemgetter(1))

ans = 1
now = a[0][1]
for l,r in a[1:]:
    if now<=l:
        ans += 1
        now = r
print(ans)