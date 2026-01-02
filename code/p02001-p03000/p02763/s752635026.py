

N = [int(i) for i in input().split()][0]
string = list(input())
Q = [int(i) for i in input().split()][0]
queries = [[i for i in input().split()] for _ in range(Q)]

tmp = N 
c = 0
while tmp > 0:
  c += 1
  tmp //= 2
N2 = 2**c
offset = N2 - 1

seg_tree = [0 for _ in range(N2*2 -1)]
for n in range(N):
  ind = ord(string[n]) - ord("a")
  seg_tree[offset + n] = 1 << ind

def set_seg_tree(i, seg_trees):
  if i >= N2 -1:
    return seg_trees[i]
  left = 2*i + 1
  right = 2*i + 2
  l_seg = set_seg_tree(left, seg_trees)
  r_seg = set_seg_tree(right, seg_trees)
  seg_trees[i] = l_seg | r_seg
  return seg_trees[i]
set_seg_tree(0, seg_tree)
    
def update(i, c, seg_trees):
  i += offset
  seg_trees[i] = 1 << c
  while i > 0:
    i = (i - 1)//2
    seg_trees[i] = seg_trees[i * 2 + 1] | seg_trees[i * 2 + 2]

def get_sum(a, b, k, l, r, seg_trees):
  if (b <= l) or (r <= a):
    return 0
  if (a <= l) and (r <= b):
    return seg_trees[k]
  vl = get_sum(a, b, k * 2 + 1, l, (l + r)//2, seg_trees)
  vr = get_sum(a, b, k * 2 + 2, (l + r)//2, r, seg_trees)
  return vl | vr

for query in queries:
  type_, i, q = query
  if type_ == "1":
    i = int(i) - 1
    pos = ord(q) - ord("a")
    update(i, pos, seg_tree)
  else:
    l = int(i) - 1
    r = int(q)
    ret = get_sum(l, r, 0, 0, N2, seg_tree)
    print(bin(ret).count("1"))
