from bisect import*
def _add(data, k, x):
    while k <= N:
        data[k] += x
        k += k & -k
def add(l, r, x):
    _add(data0, l, -x*(l-1))
    _add(data0, r, x*(r-1))
    _add(data1, l, x)
    _add(data1, r, -x)

def _get(data, k):
    s = 0
    while k:
        s += data[k]
        k -= k & -k
    return s
def query(l, r):
    return _get(data1, r-1) * (r-1) + _get(data0, r-1) - _get(data1, l-1) * (l-1) - _get(data0, l-1)
N,d,a,*t=map(int,open(0).read().split())
N+=1
z=sorted(zip(*[iter(t)]*2))
data0=[0]*(N+1)
data1=[0]*(N+1)
y=[x for x,_ in z]
c=0
for i,(x,h)in enumerate(z,1):
    h-=query(i,i+1)
    t=0--max(0,h)//a
    j=bisect(y,x+d+d)
    add(1,j+1,t*a)
    c+=t
print(c)