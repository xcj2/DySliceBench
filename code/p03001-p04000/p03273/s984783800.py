def removeRow(s, i):
  return s[:i] + s[i+1:]

def removeCol(s, j):
  for i in range(len(s)):
    s[i] = s[i][:j] + s[i][j+1:]
  return s

def isWhiteRow(s, i):
  return s[i].count("#") == 0

def isWhiteCol(s, j):
  res = True
  for i in range(len(s)):
    res &= s[i][j] == "."
  return res

H, W = map(int, input().split())
a = [ input() for _ in range(H) ]

while True:
  changed = False
  for i in range(len(a)):
    if isWhiteRow(a, i):
      a = removeRow(a, i)
      changed = True
      break
  for j in range(len(a[0])):
    if isWhiteCol(a, j):
      a = removeCol(a, j)
      changed = True
      break
  if not changed:
    for s in a:
      print(s)
    exit()
