#親要素を示す
par = {}
sum_union = {}
len_union = {}

# 初期化 -- すべての要素が根である --
def init(n):
  for i in range(n):
    par[i] = i
    sum_union[i] = Cs[i]
    len_union[i] = 1
  return 
  
# 根を求める
def root(x):
  if par[x] == x:
    return x
  else:
    #根の直下にxを置く
    par[x] = root(par[x])
    return par[x]

#　同じ集合に属するかどうかは根が同じかで判定
def same(x, y):
  return root(x) == root(y)

#　別々のUnion同士を融合する
def unite(x, y):
  rx = root(x)
  ry = root(y)
  if rx == ry:
    return
  else:
    par[rx] = ry
    tmp_sum = sum_union[rx] + sum_union[ry]
    tmp_len = len_union[rx] + len_union[ry]
    sum_union[ry] = tmp_sum
    len_union[ry] = tmp_len
    return
  
N, K = map(int, input().split())
Ps = list(map(lambda x: int(x) - 1, input().split()))
Cs = list(map(int, input().split()))


init(N)

# 結合
for i in range(N):
  unite(i, Ps[i])
  
max_result = -(10**9+1)
for i in range(N):
  ri = root(i)
  if sum_union[ri] <= 0:
    partial_range = min(K, len_union[ri])
    roop_sum = 0
  elif K < len_union[ri]:
    partial_range = K
    roop_sum = 0
  else:
    partial_range = (K % len_union[ri]) + len_union[ri]
    roop_sum = sum_union[ri] * ((K // len_union[ri])-1)
  pc = i
  sum_list = []
  sum_c = 0
  for _ in range(partial_range):
    pn = Ps[pc]
    sum_c += Cs[pn]
    sum_list.append(sum_c)
    pc = pn
    
  max_result = max(max_result, roop_sum + max(sum_list))
  
print(max_result)
  


