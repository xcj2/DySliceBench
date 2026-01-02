import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

from math import factorial
def combination(n, r):
    return factorial(n)//(factorial(n-r) * factorial(r))


h,w,k = readints()
c = [readstr() for i in range(h)]

ans = 0
for i in range(1<<h):
    for j in range(1<<w):
        black = 0
        for x in range(h):
            for y in range(w):
                if 1<<x & i and 1<<y & j and c[x][y]=='#':
                    black += 1
        if black == k:
            ans += 1

print(ans)

