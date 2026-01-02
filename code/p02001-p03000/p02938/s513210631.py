l,r = map(int,input().split())
lb = l.bit_length()
rb = r.bit_length()
ans = 0
mod = 10**9+7
def ignorel(r):
  ret = 0
  cntr = 0
  rb = r.bit_length()
  for i in range(rb-1)[::-1]:
    if r&1<<i:
      ret += 2**cntr*3**i
      cntr += 1
  ret += 2**cntr
  return ret%mod
def ignorer(l):
  cntl = 0
  ret = 0
  lb = l.bit_length()
  for i in range(lb)[::-1]:
    if l&1<<i == 0:
      ret += 2**cntl*3**i
      cntl += 1
  ret += 2**cntl
  return ret%mod
for i in range(lb+1,rb):
  ans += 3**(i-1)
  ans %= mod
if lb != rb:
  ans += ignorer(l)
  ans += ignorel(r)
  ans %= mod
  print(ans)
else:
  def from0(x):
    if x == 0:
      return 1
    elif x == 1:
      return 3
    xb = x.bit_length()
    ret = 3**(xb-1)+2*from0(x-(1<<(xb-1)))
    return ret
  def calc(l,r):
    ret = 0
    lb = l.bit_length()
    rb = r.bit_length()
    if l > r:
      return 0
    if l == r:
      return 1
    if l == 2**(lb-1):
      return ignorel(r)
    elif r == 2**rb-1:
      return ignorer(l)
    for i in range(lb)[::-1]:
      if l&1<<i == 0 and r&1<<i:
        ret += from0((1<<i)-1-(l&(1<<i)-1))
        ret += from0(r&((1<<i)-1))
        ret += calc((l&((1<<i)-1))+(1<<i),(r&((1<<i)-1))+(1<<i))
        break
    return ret%mod
  ans += calc(l,r)
  print(ans%mod)