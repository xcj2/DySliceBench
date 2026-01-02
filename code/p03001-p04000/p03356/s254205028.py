def i1():
 return int(input())
def i2():
 return [int(i) for i in input().split()]
[n,m]=i2()
p=i2()

import sys
sys.setrecursionlimit(10000)

par=[i for i in range(n)]
rank=[0 for i in range(n)]

def rt(x):
 if par[x]==x:
    return x
 else:
    par[x]=rt(par[x])
    return par[x]

def un(x,y):
    x=rt(x)
    y=rt(y)
    if x==y:
       return
    else:
       if rank[x]<rank[y]:
          par[x]=y
       else:
          par[y]=x
          if rank[x]==rank[y]:
             rank[x]+=1

       
for i in range(m):
 [x,y]=i2()
 un(x-1,y-1)

s=0
for i in range(n):
 if rt(i)==rt(p[i]-1):
   s+=1
print(s)
   
