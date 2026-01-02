X, Y, Z, K = map(int, input().split())
x_list = list(map(int, input().split()))
y_list = list(map(int, input().split()))
z_list = list(map(int, input().split()))

x_list = sorted(x_list, reverse=True)
y_list = sorted(y_list, reverse=True)
z_list = sorted(z_list, reverse=True)

# 次にとるindexの管理
next_dict = {}

def sumxyz(tup):
  return x_list[tup[0]] + y_list[tup[1]] + z_list[tup[2]]

def argmax(l):
  mxi = -1
  mx = -1
  for i, v in enumerate(l):
    if v >= mx:
      mx = v
      mxi = i
  return mxi

def add_next(tup):
  def add_not_exist(ntup):
    sm = sumxyz(ntup)
    if ntup not in next_dict:
	    next_dict[ntup] = sm
    
  if tup[0] < len(x_list)-1:
    ntup = (tup[0]+1, tup[1], tup[2])
    add_not_exist(ntup)
  if tup[1] < len(y_list)-1:
    ntup = (tup[0], tup[1]+1, tup[2])
    add_not_exist(ntup)
  if tup[2] < len(z_list)-1:
    ntup = (tup[0], tup[1], tup[2]+1)
    add_not_exist(ntup)

for i in range(K):
  if i == 0:
    print(sumxyz((0,0,0)))
    add_next((0,0,0))
  else:
    v = next_dict.values()
    k = list(next_dict.keys())
    max_idx = argmax(v)
    print(next_dict[k[max_idx]])
    next_dict[k[max_idx]] = -1
    
    add_next(k[max_idx])
