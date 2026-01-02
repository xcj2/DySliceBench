N = int(input())
h = [0] + list(map(int, input().split()))
a = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)
#####単位元######
ide_ele = 0

#num:n以上の最小の2のべき乗
num = 2 ** (N).bit_length()
seg = [ide_ele] * 2 * num

def segfunc(x, y):
  return max(x, y) #ここ判定関数（ただし結合則があるもの）

def init(init_val):
  #set_val
  for i in range(N):
    seg[i + num - 1] = init_val[i]    
  #built
  for i in range(num - 2, -1, -1) :
    seg[i]=segfunc(seg[2 * i + 1], seg[2 * i + 2]) 
    
def update(k, x):
  k += num - 1
  seg[k] = x
  while k + 1:
    k = (k - 1) // 2
    seg[k] = segfunc(seg[k * 2 + 1], seg[k * 2 + 2])
    
def query(p, q):
  if q <= p:
    return ide_ele
  p += num - 1
  q += num - 2
  res = ide_ele
  while q - p > 1:
    if p & 1 == 0:
      res = segfunc(res, seg[p])
    if q & 1 == 1:
      res = segfunc(res, seg[q])
      q -= 1
    p = p // 2
    q = (q - 1) // 2
  if p == q:
    res = segfunc(res, seg[p])
  else:
    res = segfunc(segfunc(res, seg[p]), seg[q])
  return res


for i in range(N):
  temp = query(0, h[i + 1]) + a[i + 1]
  update(h[i + 1], temp)
print(query(0, N + 2))