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
a = [readint() for i in range(n)]

ans = a[0]-1
p = 2

for i in range(1,n):
    if a[i]%p==0:
        ans += a[i]//p-1
        if a[i] == p:
            p+=1
    else:
        ans += a[i]//p

print(ans)
