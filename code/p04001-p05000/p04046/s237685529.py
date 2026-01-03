H,W,A,B=map(int,input().split())
def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    #[x,y]
    return [w[0],w[1]]
def mod_inv(a,m):
    x = extgcd(a,m)[0]
    return (m+x%m)%m
def kumi(h,w,a):
    a[0]=1
    #print(a)
    for i in range(1,h):
        b=a[i-1]*(w+i)%(10**9+7)
        a[i]=b*mod_inv(i,10**9+7)
        #print(a)
    return a
f=[0]*(H-A)
s=[0]*(H)
f=kumi(H-A,B-1,f)
s=kumi(H,W-B-1,s)
"""print(f)
print(s)"""
ans=0
for i in range(H-A):
    ans+=f[i]*s[-i-1]
print(ans%(10**9+7))
"""ans=0
for i in range(H-A):
    #print(cmb(i+B-1,B-1)%(10**9+7),cmb(H-i+W-B-2,W-B-1)%(10**9+7))
    ans+=cmb(i+B-1,B-1)*cmb(H-i+W-B-2,W-B-1)%(10**9+7)
print(ans%(10**9+7))"""
