#時系列の逆順で見る
def root(x):
    if p[x]==x:
        return x
    p[x] = y = root(p[x])
    return y
def union(x,y):
    px = root(x); py = root(y)
    if px == py:
        return
    if r[px]>r[py]:
        p[py]=px
    else:
        p[px]=py
        if r[py]==r[px]:
            r[py]+=1
def same(x,y):
    px = root(x)
    py = root(y)
    if px==py:
        return True
    else:
        return False
n,m = map(int, input().split( ))

e = []

for i in range(m):
    a,b = map(int, input().split( ))
    e.append((a,b))

e.reverse()
p = [i for i in range(n+1)]
r = [0 for i in range(n+1)]
c = [1 for i in range(n+1)]

cnt = 0
ans=[]
for i in range(m-1):
    x,y = e[i]
    if same(x,y):
        ans.append(n*(n-1)//2-cnt)
    else:
        cx = c[root(x)];cy=c[root(y)]
        union(x,y)
        cnt += (cx+cy)*(cx+cy-1)//2 - cx*(cx-1)//2 - cy*(cy-1)//2
        c[root(x)] = 0; c[root(y)]=0
        c[root(x)] = cx+cy
        ans.append(n*(n-1)//2-cnt)
ans.reverse()
for ai in ans:
    print(ai)
print(n*(n-1)//2)
    
    
