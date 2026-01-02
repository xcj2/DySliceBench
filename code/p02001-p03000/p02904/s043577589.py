N, K = list(map(int, input().split()))
P = list(map(int, input().split()))

class BITmax:
  ini = 0
  def __init__(s, num):
    s.N = 1
    while s.N <= num:
      s.N *= 2
    s.T = [s.ini] * s.N
  def set(s, L):
    for i in range(len(L)):
      s.update(i, L[i])
  def update(s, t, x):
    k = t
    s.T[k - 1] = max(s.T[k - 1], x)
    k += k & -k
    while k <= s.N:
      s.T[k - 1] = max(s.T[k - 1], x)
      k += k & -k
  def getV(s, x):
    ans = s.T[x - 1]
    x -= x & -x
    while x != 0:
      ans = max(ans, s.T[x - 1])
      x -= x & -x
    return ans

class BITmin:
  ini = N
  def __init__(s, num):
    s.N = 1
    while s.N <= num:
      s.N *= 2
    s.T = [s.ini] * s.N
  def set(s, L):
    for i in range(len(L)):
      s.update(i, L[i])
  def update(s, t, x):
    k = t
    s.T[k - 1] = min(s.T[k - 1], x)
    k += k & -k
    while k <= s.N:
      s.T[k - 1] = min(s.T[k - 1], x)
      k += k & -k
  def getV(s, x):
    ans = s.T[x - 1]
    x -= x & -x
    while x != 0:
      ans = min(ans, s.T[x - 1])
      x -= x & -x
    return ans

MA = BITmax(N)
MI = BITmin(N)

La = [0] * N
Li = [0] * N

for i in range(K - 1):
  t = N - i
  MA.update(t, P[t - 1])
  MI.update(t, P[t - 1])
for i in range(K - 2, N):
  t = N - i
  MA.update(t, P[t - 1])
  MI.update(t, P[t - 1])
  La[t - 1] = MA.getV(t + K - 2)
  Li[t - 1] = MI.getV(t + K - 2)

T = [0] * N
cnt = 0
t = 0
for i in range(1, N):
  if P[i] > P[i - 1]:
    cnt += 1
    if cnt >= K - 1:
      T[i - K + 1] = 1
      t += 1
  else:
    cnt = 0

if t != 0:
  t -= 1

for i in range(N - K):
  if T[i] == 1:
    continue
  if Li[i + 1] > P[i] and La[i + 1] < P[i + K]:
    t += 1

print(N - K - t + 1)