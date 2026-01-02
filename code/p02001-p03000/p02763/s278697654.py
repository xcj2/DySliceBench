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
  def update(s, x, n):
    k = x + 1
    s.T[k - 1] += n
    k += k & -k
    while k <= s.N:
      s.T[k - 1] += n
      k += k & -k
  def getV(s, x):
    if x <= 0: return 0
    ans = s.T[x - 1]
    x -= x & -x
    while x != 0:
      ans += s.T[x - 1]
      x -= x & -x
    return ans

N = int(input())
S = list(input())
Q = int(input())
Query = [list(input().split()) for _ in range(Q)]

B = []
R = {}

def add(i, s):
  global cnt
  if s not in R:
    b = BIT(N)
    b.update(i, 1)
    R[s] = cnt
    cnt += 1
    B.append(b)
  else:
    t = R[s]
    B[t].update(i, 1)

def minus(i, s):
  global cnt
  t = R[s]
  B[t].update(i, -1)

cnt = 0
for i in range(N):
  s = S[i]
  add(i, s)

for i in range(Q):
  q = Query[i]
  q[0] = int(q[0])
  q[1] = int(q[1])
  if q[0] == 1:
    n = q[1] - 1
    s = S[n]
    add(n, q[2])
    minus(n, s)
    S[n] = q[2]
  else:
    ans = 0
    q[2] = int(q[2])
    x, y = q[1] - 1, q[2]
    for i in range(cnt): 
      if B[i].getV(x) != B[i].getV(y):
        ans += 1
    print(ans)
    