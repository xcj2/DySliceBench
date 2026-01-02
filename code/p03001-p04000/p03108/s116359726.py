N, M = map(int, input().split())

A_list = [0]*M
B_list = [0]*M
res_list = [0]*M

for i in range(M):
  A, B = map(int, input().split())
  A_list[i] = A
  B_list[i] = B

parent_ids = list(range(N+1))
counts = [1]*(N+1)

def get_parent(i, parent_ids):
  add_list = []
  while True:
    if i == parent_ids[i]:
      break
    add_list.append(i)
    i = parent_ids[i]
  for c in add_list:
    parent_ids[c] = i
  return i

def set_parent(i, j, parent_ids, counts):
  parent_ids[i] = j
  counts[j] += counts[i]
  
def sq(n):
  return n*(n-1)//2
res_list[-1] = sq(N)

for i in range(M-1, 0, -1):
  A = A_list[i]
  B = B_list[i]
  
  ap = get_parent(A, parent_ids)
  bp = get_parent(B, parent_ids)
  a_cnt = counts[ap]
  b_cnt = counts[bp]
  
  if ap != bp:
    res_list[i-1] = res_list[i] + sq(a_cnt) + sq(b_cnt) - sq(a_cnt+b_cnt)
    set_parent(ap, bp, parent_ids, counts)
  else:
    res_list[i-1] = res_list[i]
  
  
for i in range(M):
  print(res_list[i])