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

h,w = miinps()
ans = 0
k = w%2
l = w//2
p = h//2
q = h%2

if h == 1:
  print(1)
  exit()
if w == 1:
  print(1)
  exit()
if k == 1:
  ans += (h*l)
  if q == 1:
    ans += (p+1)
  else:
    ans += p
else:
  ans += (h*l)

print(ans)