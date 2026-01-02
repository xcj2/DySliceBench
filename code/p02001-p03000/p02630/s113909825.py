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
a = readints()
q = readint()

count = Counter(a)
s = sum(a)

ans = []
for _ in range(q):
    b,c = readints()
    s += (c-b) * count[b]
    ans.append(s)
    count[c] += count[b]
    count[b] = 0
printrows(ans)


