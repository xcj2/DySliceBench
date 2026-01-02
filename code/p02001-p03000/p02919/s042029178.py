N = int(input())
P = list(map(int, input().split()))

class BIT:
  ini = 0
  def __init__(s, num):
    s.N = 1
    while s.N <= num:
      s.N *= 2
    s.T = [s.ini] * s.N
  def set(s, L):
    for i in range(len(L)):
      s.update(i, L[i])
  def update(s, x, v):
    k = x + 1
    s.T[k - 1] = max(s.T[k - 1], v)
    k += k & -k
    while k <= s.N:
      s.T[k - 1] = max(s.T[k - 1], v)
      k += k & -k
  def getV(s, x):
    if x <= 0:
      return 0
    ans = s.T[x - 1]
    x -= x & -x
    while x != 0:
      ans = max(ans, s.T[x - 1])
      x -= x & -x
    return ans

class segMin:
  inf = N + 1
  def __init__(s, num):
    s.N = 1
    while s.N < num:
      s.N *= 2
    s.T = [s.inf] * (2 * s.N - 1)
  def do(s, l, r):
    #最小値
    return min(l, r)
  def set(s, L):
    for i in range(len(L)):
      s.update(i, L[i])
  def update(s, x, v):
    k = x + s.N - 1
    s.T[k] = v
    while k > 0:
      k = (k - 1) // 2
      s.T[k] = s.do(s.T[2*k+1], s.T[2*k+2])
  def getV(s, l, r):
    if l > r:
      return s.inf
    return s.getVs(l, r, 0, 0, s.N - 1)
  def getVs(s, l, r, k, kl, kr):
    if l <= kl and r >= kr:
      return s.T[k]
    t = (kl + kr) // 2
    if l > t:
      return s.getVs(l, r, 2 * k + 2, t + 1,kr)
    if r < t + 1:
      return s.getVs(l, r , 2 * k + 1, kl, t)
    return s.do(s.getVs(l, r , 2 * k + 1, kl,t),
              s.getVs(l, r , 2 * k + 2, t + 1, kr))

ans = 0
D = [0] * (N + 1)
for i in range(N):
  D[P[i]] = i + 1

TMa = BIT(N + 1)
TMi = segMin(N + 1)

for i in range(N, 0, -1):
  #print(ans)
  t = D[i]
  ma = TMa.getV(t)
  ma2 = TMa.getV(ma)

  mi = TMi.getV(t, N + 1)
  mi2 = TMi.getV(mi + 1, N + 1)
  #print(ma2, ma, t, mi, mi2, ans)
  TMa.update(t, t)
  TMi.update(t, t)
  ans += (mi - t) * (ma - ma2) * i
  ans += (mi2 - mi) * (t - ma) * i

print(ans)
