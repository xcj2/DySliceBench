
n, q = map(int, input().split())

n_ = 1 # 実際に確保した配列のサイズ
while n_ < n:
  n_ *= 2

initv = pow(2, 31)-1
seg_tree = [initv for i in range(2*n_-1)]

def update(i, x):
  i += n_ - 1
  seg_tree[i] = x
  while i > 0 :
    i = int((i - 1)/2)
    seg_tree[i] = min(seg_tree[i*2+1], seg_tree[i*2+2])

def findMin(s, t):
  return query(s, t+1, 0, 0, n_)

def query(a, b, k, l, r):
  if r <= a or b <= l :
    return initv
  if a <= l and r <= b:
    return seg_tree[k]

  vl = query(a, b, k*2+1, l, int((l+r)/2))
  vr = query(a, b, k*2+2, int((l+r)/2), r)
  return min(vl, vr)


output = []

for i in range(q):
  line = list(map(int, input().split()))

  if line[0] == 0:
    update(line[1], line[2])

  else :
    output.append(findMin(line[1],line[2]))


for ans in output:
  print(ans)
