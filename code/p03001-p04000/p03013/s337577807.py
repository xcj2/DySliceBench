def xgcd(a, b):
    if b == 0:
        g = a
        x = 1
        y = 0
        return g, x, y
    else:
        g, s, t = xgcd(b, a%b)
        x = t
        y = s - a//b*x
        return g, x, y

def invmod(a, p):
    _, x, _ = xgcd(a, p)
    if x < 0:
        x = x + p
    return x

def count_route(n):
  if n < 0:
    return 0
  res = 0
  for i in range(n//2+1):
    res += f[n - i] * inv[i] * inv[n - 2* i]
  return res%const
    
n, m = map(int, input().split())
const = 1000000007
#nまでの階乗をハッシュテーブルに格納する
f = [1 for i in range(n + 1)]
inv = [1 for i in range(n + 1)]
for i in range(1, n+1):
  f[i] = (f[i - 1] * i)%const
  inv[i] = invmod(f[i], const)
prev = 0
ans = 1
for i in range(m):
  m = int(input())
  ans = (ans * count_route(m - 1 - prev))%const
  prev = m + 1
  if ans == 0:
    break
ans = (ans * count_route(n - prev))%const
print(ans)