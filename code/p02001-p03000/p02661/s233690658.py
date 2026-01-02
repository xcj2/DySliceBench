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
ab = [readints() for i in range(n)]


if n%2==1:
    l = -1
    r = 10**9+1
    while l+1 != r:
        m = (l+r)//2
        x = 0
        for i in range(n):
            a,b = ab[i]
            if a<=m:
                x+=1
        if x>=n//2+1:
            r = m
        else:
            l = m
    left = r
    l = -1
    r = 10**9+1
    while l+1 != r:
        m = (l+r)//2
        x = 0
        for i in range(n):
            a,b = ab[i]
            if m<=b:
                x+=1
        if x>=n//2+1:
            l = m
        else:
            r = m
    right = l
    print(right-left+1)
else:
    l = -1
    r = 10**9+1
    while l+1 != r:
        m = (l+r)//2
        x = 0
        for i in range(n):
            a,b = ab[i]
            if a<=m:
                x+=1
        if x>=n//2:
            r = m
        else:
            l = m
    left1 = r

    l = -1
    r = 10**9+1
    while l+1 != r:
        m = (l+r)//2
        x = 0
        for i in range(n):
            a,b = ab[i]
            if a<=m:
                x+=1
        if x>=n//2+1:
            r = m
        else:
            l = m
    left2 = r

    l = -1
    r = 10**9+1
    while l+1 != r:
        m = (l+r)//2
        x = 0
        for i in range(n):
            a,b = ab[i]
            if m<=b:
                x+=1
        if x>=n//2:
            l = m
        else:
            r = m
    right1 = l

    l = -1
    r = 10**9+1
    while l+1 != r:
        m = (l+r)//2
        x = 0
        for i in range(n):
            a,b = ab[i]
            if m<=b:
                x+=1
        if x>=n//2+1:
            l = m
        else:
            r = m
    right2 = l
    ans = 0
    ans += right2+right1 - left2-left1 + 1
    print(ans)





