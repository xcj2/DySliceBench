def bread_cnt(lev):
  return 2**(lev+1) - 2

def patty_cnt(lev):
  return 2**(lev+1) - 1

def burger_cnt(lev):
  return 2**(lev+2) - 3

def solve(n, x):
  return _solve(n, x, 0)
  
def _solve(n, x, p):
  total_s = burger_cnt(n)
  mid = (total_s+1)//2
  
  if x==1:
    return p + (1 if n==0 else 0)
  elif 1 < x and x <= mid:
    reach_mid = 1 if x==mid else 0
    return _solve(n-1, x-1-reach_mid, p+reach_mid)
  elif mid < x and x < total_s:
    return _solve(n-1, x-2-burger_cnt(n-1), p+1+patty_cnt(n-1))
  elif x == total_s:
    return p+patty_cnt(n)

n, x = map(int, input().split(' '))
print(solve(n,x))
