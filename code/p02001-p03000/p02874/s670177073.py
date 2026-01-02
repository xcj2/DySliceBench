N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]

def honya(LR):
  l = LR[-1][0]
  r = LR[-1][1]
  D = [0] * N
  for i in range(N - 1, -1, -1):
    l = max(l, LR[i][0])
    r = min(r, LR[i][1])
    D[i] = max(0, r - l + 1)

  l = LR[0][0]
  r = LR[0][1]
  ans = 0
  for i in range(N - 1):
    r = min(r, LR[i][1])
    ans = max(ans, max(r - l + 1, 0) + D[i + 1])

  return ans

LR.sort(reverse = True)
#for i in range(N):
#  print(LR[i], LR[i][1] - LR[i][0])
  
ans = honya(LR)

R = 0
for i in range(N):
  R = max(R, LR[i][1])
for i in range(N):
  LR[i][0], LR[i][1] = R - LR[i][1], R - LR[i][0]
  
LR.sort(reverse = True)
ans = max(ans, honya(LR))

def honyamorake(LR):
  ans = 0
  x = 0
  for i in range(N):
    t = LR[i][1] - LR[i][0] + 1
    if t > ans:
      ans = t
      x = i
  return ans + honyapun(LR, x)

def honyapun(LR, x):
  l = 0
  r = 10 ** 10
  for i in range(N):
    if i != x:
      l = max(l, LR[i][0])
      r = min(r, LR[i][1])
  if l > r:
    return 0
  else:
    return r - l + 1

ans = max(ans, honyamorake(LR))

print(ans)