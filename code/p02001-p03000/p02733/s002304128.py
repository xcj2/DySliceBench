import sys
 
MAX_INT = int(10e15)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

H,W,K = IL()
a = [list(S()) for i in range(H)]

rui = [[0]*(W+1) for i in range(H)]
for i in range(H):
  for j in range(W):
    rui[i][j+1] = rui[i][j] + int(a[i][j])
#print(rui)

ans = MAX_INT
for x in range(1<<(H-1)):
  l = 0
  num = 0
  for h in range(H-1):
    if (x >> h) & 1 == 1: # 割る
      num += 1

  for w in range(W):
    # 1行で割れるか判定
    judge = int(a[0][w])
    for h in range(H-1):
      if (x >> h) & 1 == 0: # 割らない
        judge += int(a[h+1][w])
      else: # 割る
        judge = 0
        judge += int(a[h+1][w])
      if judge > K: #どうやって割ってもダメ
        break
    else:
      continue
    break
  else:
    cnt = 0
    for w in range(W):
      #print("w:",w)
      cnt = rui[0][w+1] - rui[0][l]
      if cnt > K:
        num += 1
        l = w
        #print("break1")
        continue

      for h in range(H-1):
        #print("cnt",cnt)
        if (x >> h) & 1 == 0: # 割らない
          cnt += rui[h+1][w+1] - rui[h+1][l]
        else: # 割る
          cnt = rui[h+1][w+1] - rui[h+1][l]
        #print(rui[h+1][w+1],rui[h+1][l])

        if cnt > K:
          num += 1
          l = w
          #print("break")
          break
      #print("--")
    else:
      ans = min(ans, num)
      #print(num)

print(ans)