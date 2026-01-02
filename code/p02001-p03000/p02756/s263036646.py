def inp():
    return input()
def iinp():
    return int(input())
def inps():
    return input().split()
def miinps():
    return map(int,input().split())
def linps():
    return list(input().split())
def lmiinps():
    return list(map(int,input().split()))
def lmiinpsf(n):
    return [list(map(int,input().split()))for _ in range(n)]

s = list(inp())
q = iinp()

l = []

p = 0
o = 1

for i in range(q):
  a = inps()
  if o == 1 and a[0] == 1:
    continue
  if a[0] == "2":
    if a[1] == "1":
      if p == 0:
        l.append(a[2])
        o += 1
      else:
        s.append(a[2])
        o += 1
    else:
      if p == 0:
        s.append(a[2])
        o += 1
      else:
        l.append(a[2])
        o += 1
  if a[0] == "1":
    if p == 0:
      p = 1
    else:
      p = 0

if p == 0:
  for i in range(len(l)):
    print(l[len(l)-1-i],end="")
  for i in s:
    print(i,end="")
  print("")
else:
  for i in range(len(s)):
    print(s[len(s)-1-i],end="")
  for i in l:
    print(i,end="")
  print("")