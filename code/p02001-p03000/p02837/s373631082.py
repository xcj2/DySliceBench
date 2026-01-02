def ints():
  return [int(x) for x in input().split()]
def readi():
  return int(input())

N = readi()
SYOUGEN = [[] for _ in range(N)]

for i in range(N):
  n = readi()
  for _ in range(n):
    x, y = ints()
    x -= 1

    SYOUGEN[i].append((x, y))
  
def num1(f):
  s = 0
  while f>0:
    s += f%2
    f //= 2
  return s

def success(f):
  shoujikimono = []
  for _ in range(N):
    shoujikimono.append(f%2)
    f //= 2

  for i in range(N):
    if shoujikimono[i]:
      for x, y in SYOUGEN[i]:
        if shoujikimono[x]!=y:
          return False
  return True

maxn = 0
for f in range(2**N):
  n = num1(f)
  if success(f):
    maxn = max(maxn, n)


print(maxn)
