from collections import deque
h,w,k=map(int,input().split())
sy,sx,gy,gx=map(int,input().split())
G=[["@"]*(w+2) for i in range(h+2)]
for i in range(1,h+1):
  G[i]=["@"]+list(input())+["@"]
V=[[10**10]*(w+2) for i in range(h+2)]
V[sy][sx]=0
D=[[[0,0,0,0] for j in range(w+2)] for i in range(h+2)]
D[sy][sx]=[1,1,1,1]
X=deque([])
Y=deque([])
i=1
while G[sy-i][sx]==".":
  Y.append(sy-i)
  X.append(sx)
  V[sy-i][sx]=1
  D[sy-i][sx][0]=1
  D[sy-i][sx][1]=1
  if i==k:
    D[sy-i][sx][0]=0
    break
  i=i+1
i=1
while G[sy+i][sx]==".":
  Y.append(sy+i)
  X.append(sx)
  V[sy+i][sx]=1
  D[sy+i][sx][0]=1
  D[sy+i][sx][1]=1
  if i==k:
    D[sy+i][sx][1]=0
    break
  i=i+1

i=1
while G[sy][sx-i]==".":
  Y.append(sy)
  X.append(sx-i)
  V[sy][sx-i]=1
  D[sy][sx-i][2]=1
  D[sy][sx-i][3]=1
  if i==k:
    D[sy][sx-i][2]=0
    break
  i=i+1
i=1
while G[sy][sx+i]==".":
  Y.append(sy)
  X.append(sx+i)
  V[sy][sx+i]=1
  D[sy][sx+i][2]=1
  D[sy][sx+i][3]=1
  if i==k:
    D[sy][sx+i][3]=0
    break
  i=i+1

def yn(yy,xx):
  D[yy][xx][0]=1
  i=1
  while G[yy-i][xx]==".":
    if V[yy][xx]+1>V[yy-i][xx]:
      break
    D[yy-i][xx][0]=1
    D[yy-i][xx][1]=1
    V[yy-i][xx]=V[yy][xx]+1
    if i==k:
      D[yy-i][xx][0]=0
      Y.append(yy-i)
      X.append(xx)
      break
#    if D[yy-i][xx]!=[1,1,1,1]:
    Y.append(yy-i)
    X.append(xx)
    i=i+1


def yp(yy,xx):
  D[yy][xx][1]=1
  i=1
  while G[yy+i][xx]==".":
    if V[yy][xx]+1>V[yy+i][xx]:
      break
    D[yy+i][xx][0]=1
    D[yy+i][xx][1]=1
    V[yy+i][xx]=min(V[yy+i][xx],V[yy][xx]+1)
    if i==k:
      D[yy+i][xx][1]=0
      Y.append(yy+i)
      X.append(xx)
      break
#    if D[yy+i][xx]!=[1,1,1,1]:
    Y.append(yy+i)
    X.append(xx)
    i=i+1


def xn(yy,xx):
  D[yy][xx][2]=1
  i=1
  while G[yy][xx-i]==".":
    if V[yy][xx]+1>V[yy][xx-i]:
      break
    D[yy][xx-i][2]=1
    D[yy][xx-i][3]=1
    V[yy][xx-i]=min(V[yy][xx-i],V[yy][xx]+1)
    if i==k:
      D[yy][xx-i][2]=0
      Y.append(yy)
      X.append(xx-i)
      break
#    if D[yy][xx-i]!=[1,1,1,1]:
    Y.append(yy)
    X.append(xx-i)
    i=i+1


def xp(yy,xx):
  D[yy][xx][3]=1
  i=1
  while G[yy][xx+i]==".":
    if V[yy][xx]+1>V[yy][xx+i]:
      break
    D[yy][xx+i][2]=1
    D[yy][xx+i][3]=1
    V[yy][xx+i]=min(V[yy][xx+i],V[yy][xx]+1)
    if i==k:
      D[yy][xx+i][3]=0
      Y.append(yy)
      X.append(xx+i)
      break
#    if D[yy][xx+i]!=[1,1,1,1]:
    Y.append(yy)
    X.append(xx+i)
    i=i+1

while len(X)>0:
  x=X[0]
  y=Y[0]
  X.popleft()
  Y.popleft()
  if D[y][x][0]==0:
    yn(y,x)
  if D[y][x][1]==0:
    yp(y,x)
  if D[y][x][2]==0:
    xn(y,x)
  if D[y][x][3]==0:
    xp(y,x)

if V[gy][gx]==10**10:
  print(-1)
else:
  print(V[gy][gx])