import sys
from collections import Counter
from collections import deque
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

n,a,b,c,d=mp()
s=input()
if s[a-1]=="#" or s[b-1]=="#" or s[c-1]=="#" or s[d-1]=="#":
    print("No")
    exit()
for i in range(min(a,b)-1,max(c,d)):
    if s[i]=="#" and s[i+1]=="#":
        print("No")
        exit()
if d<c:
    ch=False
    for i in range(b-2,d-1):
        if s[i]=="." and s[i+1]=="." and s[i+2]==".":
            ch=True
    if ch:
        print("Yes")
        exit()
    else:
        print("No")
        exit()
else:
    print("Yes")
