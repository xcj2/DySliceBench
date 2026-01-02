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

ans = 10**10

only = [[[]for i in range(2*10**5+1)]for j in range(4)]
plus = [[[]for i in range(4*10**5+1)]for j in range(4)]
minus = [[[]for i in range(4*10**5+1)]for j in range(4)]
a = ['D','U','L','R']
for i in range(n):
    x,y,z = readstrs()
    x = int(x)
    y = int(y)
    b = a.index(z)
    if b<2:
        only[b][x].append(y)
    else:
        only[b][y].append(x)
    plus[b][x+y].append(x)
    minus[b][x-y].append(x)

def keisan(a,b,ans):
    a.sort()
    b.sort()
    k = 0
    j = 0
    while k<len(a) and j<len(b):
        if a[k]>b[j]:
            ans = min(ans,a[k]-b[j])
            j += 1
        else:
            k += 1
    return ans

for m in [0,2]:
    for i in range(2*10**5+1):
        a = only[m][i]
        b = only[m+1][i]
        if a and b:
            ans = keisan(a,b,ans)

if ans != 10**10:
    ans/=2

for p,q in [[2,1],[0,3]]:
    for i in range(4*10**5+1):
        a = minus[p][i]
        b = minus[q][i]
        if a and b:
            ans = keisan(a,b,ans)

for p,q in [[1,3],[2,0]]:
    for i in range(4*10**5+1):
        a = plus[p][i]
        b = plus[q][i]
        if a and b:
            ans = keisan(a,b,ans)

if ans == 10**10:
    print('SAFE')
else:
    print(int(ans*10))
