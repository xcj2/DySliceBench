n, q = map(int, input().split())
p = [-1]*n

def root(x):
    if p[x]==-1:
        return x
    
    p[x] = root(p[x])
    return p[x]

def unite(a, b):
    if root(a)!=root(b):
        if a>b:
            a,b = b,a
        p[root(b)] = root(a)
        
def same(a, b):
    if root(a)==root(b):
        return True
    else:
        return False
    
for i in range(q):
    c, a, b = map(int, input().split())
    if c==0:
        unite(a, b)
       # print(p)
    if c==1:
        if same(a, b):
            print(1)
        else:
            print(0)
