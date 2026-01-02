n, x = map(int, input().split())
ans = 0

def burger(n):
  if n == 0:
    return 'P'
  else:
    s = burger(n-1)
    return 'B' + s + 'P' + s + 'B'
  
def layer(n):
  return 2**(n+2)-3 # 層の数

def layhalf(n):
  return 2**(n+1)-2 # 中央のパテよりも下（上）にある層数

def pate(n):
  return 2**(n+1)-1 # パテの数

def search(n, x):
  global ans
  
  if x <= 0:
    pass
  elif layer(n) - n <= x:
    ans += pate(n)
  elif layhalf(n) + 1 <= x:
    ans += pate(n - 1) + 1
    search(n - 1, x - layhalf(n) - 1)
  elif layhalf(n) == x:
    ans += pate(n - 1)
  else:
    search(n - 1, x - 1)
    
search(n, x)
print(ans)