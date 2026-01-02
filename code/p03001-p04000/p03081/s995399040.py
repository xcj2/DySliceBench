import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))


n,q = readints()
s = readstr()
td = [readstrs() for i in range(q)]

l = -1
r = n
while l+1<r:
    m = (l+r)//2
    now = m
    for t,d in td:
        if s[now] == t:
            if d=='L':
                now -=1
            else:
                now += 1
            if now<0 or now>=n:
                break
    if now <0:
        l = m
    else:
        r = m
left = l

l = -1
r = n
while l+1<r:
    m = (l+r)//2
    now = m
    for t,d in td:
        if s[now] == t:
            if d=='L':
                now -=1
            else:
                now += 1
            if now<0 or now>=n:
                break
    if now >= n:
        r = m
    else:
        l = m
right = r

print(right-1-left)

