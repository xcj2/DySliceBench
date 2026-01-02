from collections import deque

h,w=map(int,input().split())
ch,cw=map(int,input().split())
dh,dw=map(int,input().split())

ch-=1
cw-=1
dh-=1
dw-=1

S=[]
for _ in range(h):
  s=input()
  sl=[]
  for i in range(w):
    sl.append(s[i])
  S.append(sl)

def isable(X):
  xh,xw=X[0],X[1]
  if 0<=xh<=h-1 and 0<=xw<=w-1 and S[xh][xw]=='.':
    return True
  else:
    return False

def stepA(X):
  xh,xw=X[0],X[1]
  A=[]
  for p,q in [(-1,0),(0,1),(1,0),(0,-1)]:
    if isable([xh+p,xw+q]):
      A.append([xh+p,xw+q])
  return A
    
def stepB(X):
  xh,xw=X[0],X[1]
  B=[]
  for i in range(-2,3):
    for j in range(-2,3):
      if i==0 and j==0:
        continue
      if isable([xh+i,xw+j]):
        B.append([xh+i,xw+j])
  return B

Q=deque()
Q.appendleft((ch,cw))
cost=[[float('inf') for i in range(w)] for j in range(h)]
cost[ch][cw]=0

while Q:
  ph,pw=Q.popleft()
  for v in stepA([ph,pw]):
    ah,aw=v[0],v[1]
    if isable([ah,aw]):
      if cost[ah][aw]>cost[ph][pw]:
        cost[ah][aw]=cost[ph][pw]
        Q.appendleft([ah,aw])
  for bh,bw in stepB([ph,pw]):
    if isable([bh,bw]):
      if cost[bh][bw]>cost[ph][pw]+1:
        cost[bh][bw]=cost[ph][pw]+1
        Q.append([bh,bw])

if cost[dh][dw]==float('inf'):
  print(-1)
else:
  print(cost[dh][dw])