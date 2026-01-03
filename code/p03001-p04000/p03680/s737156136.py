def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

import sys
sys.setrecursionlimit(1000000)

n = ii()
s = set()
l = []
cnt = 0
def solve(index,cnt):
    if l[index] == 2:
        print(cnt+1)
        exit()
    elif l[index] in s:
        print(-1)
        exit()
    else:
        s.add(l[index])
        solve(l[index]-1,cnt+1)
    return 0

for i in range(n):
    num = ii()
    l.append(num)

solve(0,cnt)

