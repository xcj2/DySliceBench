import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

n,m = readints()
x = readints()
modx = [i%m for i in x]

a = [0]*(10**5+1)
b = [0]*m
for i in range(n):
    a[x[i]]+=1
    b[modx[i]]+=1

ans = b[0]//2
b[0] = 0
y = m//2
if m%2==0:
    ans += b[m//2]//2
    b[m//2] = 0
else:
    y += 1
for i in range(1,y):
    c = min(b[i],b[m-i])
    b[i] -= c
    b[m-i] -= c
    ans += c
for i in range(10**5+1):
    if b[i%m]>1 and a[i]>1:
        c = min(b[i%m],a[i])//2
        ans += c
        b[i%m] -= c*2

print(ans)
