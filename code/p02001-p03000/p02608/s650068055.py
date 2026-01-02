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

ans = [0]*(n+1)

for x in range(1,101):
    for y in range(1,101):
        for z in range(1,101):
            a = x**2+y**2+z**2+x*y+x*z+z*y
            if a<=n:
                ans[a] += 1

printrows(ans[1:])




