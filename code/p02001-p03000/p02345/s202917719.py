INF = 10 ** 20

n, q = map(int, input().split())

size = 1
while size < n:
  size *= 2
size = size * 2 - 1

seg_tree = [2 ** 31 - 1 for _ in range(size)]

def update(i, x):
  ind = size // 2 + i 
  seg_tree[ind] = x
  while ind:
    ind = (ind - 1) // 2
    ch1 = seg_tree[ind * 2 + 1]
    ch2 = seg_tree[ind * 2 + 2]
    seg_tree[ind] = min(ch1, ch2)

def _find(s, t, k, l, r):
  if r < s or t < l: return INF
  if s <= l and r <= t:
    return seg_tree[k]
  else:
    vl = _find(s, t, k * 2 + 1, l, (l + r) // 2)
    vr = _find(s, t, k * 2 + 2, (l + r) // 2 + 1, r)
    return min(vl, vr)

def find(s, t):
  return _find(s, t, 0, 0, size // 2)

for _ in range(q):
  com, x, y = map(int, input().split())
  if not com:
    update(x, y)
  else:
    print(find(x, y))
