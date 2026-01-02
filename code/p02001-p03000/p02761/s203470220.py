import sys

readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))


n,m = readints()

ans = [-1]*n

flag = 1
for i in range(m):
    s,c = readints()
    s-=1
    if s==c==0 and n!=1:
        flag = 0
        break
    elif ans[s] == -1:
        ans[s]=c
    elif ans[s]!=c:
        flag = 0
        break

if flag:
    if ans[0]==-1:
        if n==1:
            ans[0]=0
        else:
            ans[0]=1
    ans = [x if x>=0 else 0 for x in ans]
    print(''.join(map(str,ans)))
else:
    print(-1)