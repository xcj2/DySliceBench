N, M = map(int, input().split())
D = [None] * M
for i in range(M):
  a, b = map(int, input().split())
  D[i] = (a, b)
D.reverse()

P = list(range(N))
C = [1] * N
R = [1] * N
def root(x):
  if P[x] == x:
    return x
  else:
    rx = root(P[x])
    P[x] = rx
    return rx

def find(x, y):
  return root(x) == root(y)

def union(x, y):
  rx = root(x)
  ry = root(y)
  if rx != ry:
    if R[ry] > R[rx]:
      rx, ry = ry, rx
    P[ry] = rx
    C[rx] += C[ry]
    R[rx] = max(R[rx], R[ry] + 1)

def size(x):
  return C[root(x)]

f = N * (N - 1) // 2
F = []
for a, b in D:
  a -= 1
  b -= 1
  F.append(f)
  if not find(a, b):
    f = max(0, f - size(a) * size(b))
    union(a, b)

F.reverse()
for f in F:
  print(f)