def columnCheck(a):
  result = False
  for i in a:
    if i == [0, 0, 0]:
      result = True
  return result

def rowCheck(a):
  result = False
  for j in range(3):
    if a[0][j] == 0 and a[1][j] == 0 and a[2][j] == 0:
      result = True
  return result

def crossCheck(a):
  result = False
  if a[0][0] == 0 and a[1][1] == 0 and a[2][2] == 0:
    result = True
  if a[0][2] == 0 and a[1][1] == 0 and a[2][0] == 0:
    result = True
  return result

a = []
for i in range(3):
  a.append([int(i) for i in input().split(" ")])
n = int(input())
b = []
for i in range(n):
  b.append(int(input()))

for num in b:
  for i in range(3):
    for j in range(3):
      if a[i][j] == num:
        a[i][j] = 0

print("Yes" if columnCheck(a) or rowCheck(a) or crossCheck(a) else "No")