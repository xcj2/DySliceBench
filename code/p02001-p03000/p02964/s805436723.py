import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))


import bisect

n,k = readints()

a = readints()

place = [[] for i in range(max(a)+1)]

for i,x in enumerate(a):
    place[x].append(i)

now = 0
i = 1
while k>1:
    x = a[now]
    if now >= place[x][-1]:
        i+=1
        k-=1
        now = place[x][0]+1
    else:
        now = place[x][bisect.bisect_right(place[x],now)] + 1
    if now == n:
        now = 0
        k-=1
        k%=i
        if k<1:
            k+=i

ans = []
while now <= n-1:
    x = a[now]
    if now >= place[x][-1]:
        ans.append(x)
        now += 1
    else:
        now = place[x][bisect.bisect_right(place[x],now)] + 1

printline(ans)
















