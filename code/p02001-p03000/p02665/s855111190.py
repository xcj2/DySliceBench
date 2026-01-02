def N(): return int(input())
def NM():return map(int,input().split())
def L():return list(NM())
def LN(n):return [N() for i in range(n)]
def LL(n):return [L() for i in range(n)]
def Yes(x):print("Yes")if x==True else print("No")
n=N()
l=L()
if n==0:
    if l[0]==1:
        print(1)
    else:
        print(-1)
    quit()
if l[0]==1:
    if sum(l)==1:
        print(1)
    else:
        print(-1)
    quit()
ans=[0]*(n+1)
v=1
ans[0]=1
for i in range(1,n+1):
    v*=2
    ans[i]=v
    v-=l[i]
    if v<0:
        print(-1)
        quit()
for i in range(n,0,-1):
    ans[i]-=v
    if ans[i]>=ans[i-1]-l[i-1]:
        break
    v=ans[i-1]-l[i-1]-ans[i]
print(sum(ans))