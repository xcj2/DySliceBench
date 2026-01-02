A, B, C, D, E , F = map(int, input().split())

def makeSet(a, b):
  list = []
  for i in range(int(F / a + 2)):
    for j in range(int(F / b + 2)):
      tmp = i * a + j * b
      if tmp > F:
        break
      list.append(tmp)
  return set(list)

W = makeSet(A * 100, B * 100)
S = makeSet(C, D)

def isOK(a, b):
  return b * (100 + E) <= E * (a + b) and a + b <= F

ma = F
mb = 0

def chmax(a, b):
  if b * (ma + mb) >= mb * (a + b):
    return a, b
  return ma, mb

for w in W:
  for s in S:
    if isOK(w, s):
      ma, mb = chmax(w, s)

print(ma + mb, mb)