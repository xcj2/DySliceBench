N, M = map(int, input().split())
I = [[i, 1] for i in range(N)]
B = [0] * M
for i in range(M):
  B[M - 1 - i] = [int(x) - 1 for x in input().split()]
NC = [0] * M
def n2(n):
  return n * (n - 1) // 2
NC[-1] = n2(N)
def root(a):
  #print(a, I[a][0])
  if I[a][0] == a:
    return a
  else:
    I[a][0] = root(I[a][0])
    return I[a][0]
def union(a, b):
  ra = root(a)
  rb = root(b)
  na = I[ra][1]
  nb = I[rb][1]
  if ra == rb:
    return 0
  if ra < rb:
    I[rb][0] = ra
    I[ra][1] += I[rb][1]
  else:
    I[ra][0] = rb
    I[rb][1] += I[ra][1]
  return n2(na + nb) - n2(na) - n2(nb)
for i in range(M - 1):
  a, b = B[i]
  NC[M - 2 - i] = NC[M - 1 - i] - union(a, b)
for nc in NC:
  print(nc)