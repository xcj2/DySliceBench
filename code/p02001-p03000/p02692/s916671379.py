import sys
from functools import lru_cache
from collections import defaultdict
from collections import deque
inf = float('inf')
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().rstrip()
def read():
  return int(readline())
def reads():
  return map(int, readline().split())
n,a,b,c=reads()
lsAB=deque()
lsBC=deque()
lsAC=deque()
dic=defaultdict(int)
k=-1
lsS=[]
for i in range(n):
  s=input()
  lsS.append(s)
  if "AB" in s:
    lsAB.append(i)
    a-=1
    b-=1
  if "BC" in s:
    lsBC.append(i)
    b-=1
    c-=1
  if "AC" in s:
    lsAC.append(i)
    c-=1
    a-=1
  if a<0:
    a+=2
    try:
      hoge=lsAB[0]
    except:hoge=inf
    try:
      hoge2=lsAC[0]
    except:hoge2=inf   
    #print(hoge,hoge2)
    if min(hoge,hoge2)>i:
      print("No")
      exit()
    if hoge<hoge2:
        dic[hoge]=0
        lsAB.popleft()
    else:
        dic[hoge2]=0
        lsAC.popleft()
  if b<0:
    b+=2
    try:
      hoge=lsAB[0]
    except:hoge=inf   
    try:
      hoge2=lsBC[0]
    except:hoge2=inf   
    if min(hoge,hoge2)>i:
      print("No")
      exit()
    if hoge<hoge2:
        dic[hoge]=1
        lsAB.popleft()
    else:
        dic[hoge2]=0
        lsBC.popleft()
  if c<0:
    c+=2
    try:
      hoge=lsBC[0]
    except:hoge=inf
    try:
      hoge2=lsAC[0]
    except:hoge2=inf   
    #print(hoge,hoge2)
    if min(hoge,hoge2)>i:
      print("No")
      exit()
    if hoge<hoge2:
        dic[hoge]=1
        lsBC.popleft()
    else:
        dic[hoge2]=1
        lsAC.popleft()
print("Yes")
for i in range(n):
  print(lsS[i][dic[i]])
