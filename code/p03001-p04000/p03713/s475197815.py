def sp(n):
  a = n // 3
  b = (n - a) // 2
  c = n -a -b
  return a,b,c

def ceil(x, y):
  return (x -1) // y + 1

def tatedake_diff(h, w):
  a,b,c = sp(h)
  s1 = (c-a) * w
  a,b,c = sp(w)
  s2 = (c-a) * h
  return min(s1, s2)

def tateyoko_diff(h, w):
  a,b,c = sp(h)
  s1 = (c * w)
  s2 = (h - c) * (w // 2)
  s3 = (h - c) * ceil(w, 2)
  r1 = max(s1,s2,s3) - min(s1,s2,s3)
  s1 = (a * w)
  s2 = (h - a) * (w // 2)
  s3 = (h - a) * ceil(w, 2)
  r2 = max(s1,s2,s3) - min(s1,s2,s3)
  return min(r1,r2)
  
H, W = map(int, input().split())
if H % 3 == 0 or W % 3 == 0:
  ans = 0
else:
  ans = min(tatedake_diff(H, W), tateyoko_diff(H, W), tateyoko_diff(W, H))
print(ans)