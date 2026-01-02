import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

def dist(x,y):
    return min(abs(x-y), abs(24-abs(x-y)))

n = readint()
d = readints()

d.sort()

a = [0]*24
a[0]=1
for i in range(n):
    if d[i]==0:
        a[0]+=1
        continue
    if d[i]==12:
        a[12]+=1
        continue
    x = d[i]
    y = 24-d[i]
    ansx = 100
    ansy = 100
    for j in range(24):
        if a[j]:
            ansx = min(ansx, dist(x,j))
            ansy = min(ansy,dist(y,j))
    if ansx >= ansy:
        a[x]+=1
    else:
        a[y]+=1

ans = 100
for x in a:
    if x>1:
        ans = 0

if ans:
    b = []
    for i,x in enumerate(a):
        if x:
            b.append(i)
    for i in range(len(b)):
        ans = min(ans,dist(b[i],b[i-1]))
print(ans)

    






