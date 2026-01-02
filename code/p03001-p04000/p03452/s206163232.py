n, m = map(int,input().split())
par=[i for i in range(n)]
ws =[0 for _ in range(n)]

def root(x):
    if par[x]==x:
        return x
    else:
        r =root(par[x])
        ws[x] +=ws[par[x]]
        par[x]=r
        return par[x]

def weight(x):
    root(x)
    return ws[x]
def diff(x,y):
    return weight(x) -weight(y)

def merge(x,y,w):
    if root(x)==root(y):
        if diff(x,y)!=w:
            print('No')
            exit()
        else:
            return
    else:
        wy=weight(y)
        wx=weight(x)
        x=root(x)
        y=root(y)
        if w+wy>=wx:
            
            par[x]=y
            ws[x]=w+wy-wx
        else:
            par[y]=x
            ws[y]=wx-w-wy

for _ in range(m):
    x,y,z= map(int,input().split())
    x -=1
    y -=1
    merge(x,y,z)

print('Yes')