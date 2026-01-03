N = int(input())
p = [None]+[int(c) for c in input().split()]
p_to_i = [None]*(N+1)
for i, x in enumerate(p[1:],1):
  p_to_i[x] = i

tree = [0]*(N+1)

def BIT_add(i):
  while i<=N:
    tree[i] += 1
    i += i&(-i)
    
def BIT_sum(i):
  s = 0
  while 0<i:
    s += tree[i]
    i -= i&(-i)
  return s

def BIT_search(c):
  s = 0
  step = 1<<(N.bit_length()-1)
  i = 0
  while step:
    if i+step<=N and s+tree[i+step]<c:
      i += step
      s += tree[i]
    step >>= 1
  return i+1

ans = 0
for i in range(1,N+1):
  c = p_to_i[i]
  L = BIT_sum(c)
  R = i-1-L
  BIT_add(c)
  a = BIT_search(L) if L>0 else 0
  b = BIT_search(L+2) if R>0 else N+1
  m = (c-a)*(b-c)
  ans += m*i
#  print(i, ans, a, b, c, L, R)
print(ans)
  