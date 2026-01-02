import sys
from collections import Counter
from collections import deque
import math
import fractions
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

n=int(input())
l=[lmp() for i in range(n)]
if l[0][0]<l[0][1]+l[0][2] or l[0][0]%2!=(l[0][1]+l[0][2])%2:
    print("No")
    exit()
for i in range(n-1):
    t,x,y=l[i+1][0]-l[i][0],abs(l[i+1][1]-l[i][1]),abs(l[i+1][2]-l[i][2])
    if t<x+y or t%2!=(x+y)%2:
        print("No")
        exit()
print("Yes")