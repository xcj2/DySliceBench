import sys
from collections import Counter
from collections import deque
import heapq
import math
import fractions
import bisect
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

h,w,d=mp()
l=[[]for i in range(h*w+1)]
for i in range(h):
    a=lmp()
    for k in range(w):
        l[a[k]]=[i,k]
ans=[0]*(h*w+1)
for i in range(1,d+1):
    for k in range((h*w-i)//d):
        ans[i+(k+1)*d]=ans[i+k*d]+abs(l[i+k*d][0]-l[i+(k+1)*d][0])+abs(l[i+k*d][1]-l[i+(k+1)*d][1])
q=int(input())
for i in range(q):
     l,r=mp()
     print(ans[r]-ans[l])
