def mul(a,b,p):
    return ((a % p) * (b % p)) % p

def div(a,b,p):
    return mul(a, power_func(b, p-2,p),p)

def power_func(a,n,p):
  bi=str(format(n,"b"))
  res=1
  for i in range(len(bi)):
    res=(res*res) %p
    if bi[i]=="1":
      res=(res*a) %p
  return res

modp = 1000000007
_ = input()
s = input()
d = dict()
for c in s:d[c] = d.get(c,0)+1

g = power_func(2,len(d),modp)
g = (g+modp-1) % modp

for c in sorted(d.keys()):
    subsubg = div((g+1)%modp,2,modp)
    subg = (subsubg % modp) * ((d[c]-1)%modp) % modp
    g = (g + subg) % modp
print(g)