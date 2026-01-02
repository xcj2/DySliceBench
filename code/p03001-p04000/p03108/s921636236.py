N, M = map(int, input().split())
ABs = []
for i in range(M):
  A, B = map(int, input().split())
  A, B = A-1, B-1
  ABs.append((A, B))
UF = list(range(N))
Ns = [1]*N
def par(m):
  s = []
  r = UF[m]
  while r != m:
    s.append(m)
    m = r
    r = UF[m]
  for i in s:
    UF[i] = r
  return r
def unite(m, n):
  i = par(m)
  j = par(n)
  UF[j] = i
  Ns[i] = Ns[j] = Ns[i]+Ns[j]
def size(m):
  return Ns[par(m)]
r = N*(N-1)//2
rs = [r]
for A, B in reversed(ABs):
  if par(A) == par(B):
    rs.append(r)
    continue
  sA = size(A)
  sB = size(B)
  unite(A, B)
  r -= sA*sB
  rs.append(r)
rs.pop()
for r in reversed(rs):
  print(r)
