import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

n  =readint()
a = readints()

if n%2==0:
    b = 0
    for i in range(n):
        b^=a[i]
    ans = [b^a[i] for i in range(n)]
else:
    b = a[0]
    ans = [0]+[b^a[i] for i in range(1,n)]

printline(ans)

