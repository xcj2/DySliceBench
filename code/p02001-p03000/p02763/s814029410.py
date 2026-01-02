#####segfunc######
def segfunc(x,y):
  return x|y 

def init(init_val):
  #set_val
  for i in range(n):
    seg[i+num-1]=init_val[i]  
  #built
  for i in range(num-2,-1,-1) :
    seg[i]=segfunc(seg[2*i+1],seg[2*i+2]) 
  
def update(k,x):
  k += num-1
  seg[k] = x
  while k:
    k = (k-1)//2
    seg[k] = segfunc(seg[k*2+1],seg[k*2+2])
  
def query(p,q):
  if q<=p:
    return ide_ele
  p += num-1
  q += num-2
  res=ide_ele
  while q-p>1:
    if p&1 == 0:
      res = segfunc(res,seg[p])
    if q&1 == 1:
      res = segfunc(res,seg[q])
      q -= 1
    p = p//2
    q = (q-1)//2
  if p == q:
    res = segfunc(res,seg[p])
  else:
    res = segfunc(segfunc(res,seg[p]),seg[q])
  return res

#####単位元######
ide_ele = set([])

#num:n以上の最小の2のべき乗
n = int(input())
S = [set([s]) for s in input()]
num =2**(n-1).bit_length()
seg=[ide_ele]*2*num

init(S)
q = int(input())
for _ in range(q):
  a,b,c = input().split()
  if a == '1':
    b = int(b)-1
    update(b, set([c]))
  elif a == '2':
    b = int(b)-1
    c = int(c)
    print(len(query(b,c)))