h,w=[int(j) for j in input().split()]
s=[input()for i in range(h)]
par=[-1 for i in range(h*w)]
def root(a):
    if par[a]<0:
        return a
    else:
        return root(par[a])

def size(a):
    return -par[root(a)]

def connect(a,b):
    a=root(a)
    b=root(b)
    if a==b:
        return False
    if size(a)<size(b):
        a,b=b,a
    par[a]+=par[b]
    par[b]=a
    return True

for i in range(h):
    for j in range(w):
        for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
            p,q=i+x,j+y
            if 0<=p<h and 0<=q<w:
                if s[p][q]!=s[i][j]:
                    if root(w*p+q)!=root(w*i+j):
                        connect(w*p+q,w*i+j)

from collections import Counter
c=Counter()
for i in range(h):
    for j in range(w):
        p=i*w+j
        q=root(p)
        if c[q]==0:
            c[q]=[0,0]
        if s[i][j]=="#":
            c[q][0]+=1
        else:
            c[q][1]+=1
ans=0
for i in c:
    ans+=c[i][0]*c[i][1]
print(ans)
