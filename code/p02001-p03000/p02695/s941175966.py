printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

def pt(s):
    sm = 0
    for i in range(q):
        if s[b[i]]-s[a[i]]==c[i]:
            sm += d[i]
    return sm

def dfs(i,s):
    if i==10:
        return pt(s)
    mx = -1
    s1 = s[-1]
    for j in range(s1,m+1):
        s.append(j)
        v = dfs(i+1,s)
        mx = max(mx,v)
        s.pop()
    return mx

n,m,q = inm()
a = []
b = []
c = []
d = []
for i in range(q):
    aa,bb,cc,dd = inm()
    a.append(aa)
    b.append(bb)
    c.append(cc)
    d.append(dd)
s = [1]
print(dfs(0,s))
