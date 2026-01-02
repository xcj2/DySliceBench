import sys
input = sys.stdin.readline
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

def tami(x, vis, c):
  global tmp
  if x == 1:
    tmp = min(tmp, c)
    return
  for i in range(10):
    if str(i) in vis:
      continue
    else:
      tami(i, vis+str(i), c+data[x][i])
    
H,W = IL()
data = [IL() for _ in range(10)]
wall = [IL() for _ in range(H)]
cost = [0]*10

for i in range(10):
  if i == 1:
    continue
  else:
    tmp = 100000
    tami(i, str(i), 0)
    cost[i] = tmp
#print(cost)

ans = 0
for h in range(H):
  for w in range(W):
    if abs(wall[h][w]) == 1:
      continue
    else:
      ans += cost[wall[h][w]]
print(ans)