#### import ####
import sys
import math
from collections import defaultdict

#### 設定 ####
sys.setrecursionlimit(10**7)
def input():
  return sys.stdin.readline()[:-1]

#### 定数 ####
mod = 10**9 + 7

#### 読み込み ####
def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
  read_all = [tuple(map(int, input().split())) for _ in range(N)]
  return map(list,zip(*read_all))

#################

def Z_algo(S):
  n=len(S)
  A=[0]*n
  A[0]=n
  i=1
  j=0
  while i<n:
    while i+j<n and S[j]==S[i+j]: j+=1
    A[i]=j
    if j==0:
      i+=1
      continue
    k=1
    while i+k<n and k+A[k]<j:
      A[i+k]=A[k]
      k+=1
    i+=k
    j-=k
  return A

def dfs(pt,v,visited):
  if visited[v]==True:
    return -1,visited
  S = [v]
  now = 0
  while S:
    v1 = S.pop()
    for i in pt[v1]:
      if i != v:
        visited[i] = True
        now += 1
        S.append(i)
      else:
        print(-1)
        exit()
  return now,visited

s = str(input())
t = str(input())

ls = len(s)
lt = len(t)

s2 = t + s*(lt//ls +2)
A = Z_algo(s2)

B = [False]*ls
for i in range(ls):
  if A[i+lt]>=lt:
    B[i]=True

pt = [[] for _ in range(ls)]
for i in range(ls):
  if B[i]==True:
    pt[i].append((i+lt)%ls)

visited = [False]*ls

ans = 0
for v in range(ls):
  if B[v]:
    tmp,visited = dfs(pt,v,visited)
    if tmp>ans:
      ans = tmp

print(ans)