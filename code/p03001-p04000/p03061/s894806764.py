def gcd(a,b):
  if a*b == 0:
    return max(a,b)
  if a<b:
    a,b = b,a
  return gcd(b,a%b)
n = int(input())
ls = list(map(int,input().split()))
length = 2**(n.bit_length())
calc = gcd
unit = 0
Seg = [unit for i in range(length*2-1)]
def init():
  for i in range(n):
    Seg[i+length-1] = ls[i]
  for i in range(length-2,-1,-1):
    Seg[i] = calc(Seg[2*i+1],Seg[2*i+2])
def update(i,x):
  i += length-1
  Seg[i] = x
  while i>0:
    i = (i-1)//2
    Seg[i] = calc(Seg[2*i+1],Seg[2*i+2])
def query(a,b,k,l,r):
  if r<=a or b<=l:
    return unit
  if l<=a and b<=r:
    return Seg[k]
  else:
    vl = query(a,b,2*k+1,l,(l+r)//2)
    vr = query(a,b,2*k+2,(l+r)//2,r)
    return calc(vl,vr)

init()
ans = []
for i in range(n):
  update(i,0)
  ans.append(query(0,n,0,0,length))
  update(i,ls[i])
print(max(ans))