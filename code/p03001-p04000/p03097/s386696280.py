def extract(a, i):
  return (a>>(i+1) << i) | (a&((1<<i)-1))

def space(a, i):
  return ((a>>i) << (i+1)) | (a&((1<<i)-1))

def compose(n, a, b):
  if n==1:
    return [a, b]
  for i in range(n):
    if (a>>i&1) ^ (b>>i&1):
      x = i
      a_bool = (a>>i & 1) << i
      b_bool = a_bool ^ (1 << i)
      a_dash = extract(a, i)
      b_dash = extract(b, i)
      c = a_dash ^ 1
      break
  Q = compose(n-1, a_dash, c)
  R = compose(n-1, c, b_dash)
  n_Q = [space(i, x)|a_bool for i in Q]
  n_R = [space(i, x)|b_bool for i in R]
  return n_Q + n_R
  
n, a, b = map(int, input().split())
cnt = 0
c = a^b
for i in range(n):
  cnt += c>>i & 1
if cnt&1:
  print("YES")
  print(*compose(n, a, b))
else:
  print("NO")