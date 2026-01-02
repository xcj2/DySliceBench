import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))


n = readint()
a = []
b = []
for i in range(n):
    x,y = readints()
    a.append(x)
    b.append(y)
a.sort()
b.sort()

if n%2==1:
    l = a[n//2]
    r = b[n//2]
    print(r-l+1)
else:
    l = a[n//2] + a[n//2-1]
    r = b[n//2] + b[n//2-1]
    print(r-l+1)