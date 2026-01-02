def gcd(xxx,yyy):
    if xxx<yyy:
        xxx,yyy=yyy,xxx
    if yyy==0:
        return xxx
    else:
        return gcd(yyy,xxx%yyy)

def seg_tree_update(n,x):
    ind=2**m-1+n
    tree[ind]=x
    ind=(ind-1)//2
    while ind>=0:
        tree[ind]=gcd(tree[2*ind+1],tree[2*ind+2])
        ind=(ind-1)//2

def seg_tree_find_gcd(L,R):
    qqq=A[L]
    L,R=2**m-1+L,2**m-1+R
    while L<R:
        if L%2==0:
            qqq=gcd(qqq,tree[L])
        if R%2==1:
            qqq=gcd(qqq,tree[R])
        L//=2
        R=R//2-1
        
    if L==R:
        qqq=gcd(qqq,tree[L])
    return qqq

N=int(input())
A=list(map(int,input().split()))
inf=float("inf")
m=0
while pow(2,m)<N:
    m+=1
tree=[0]*(pow(2,m+1)-1)

for i in range(N):
    seg_tree_update(i,A[i])
    
ans=max(seg_tree_find_gcd(1,N-1),seg_tree_find_gcd(0,N-2))
for i in range(1,N-1):
    ddd=gcd(seg_tree_find_gcd(0,i-1),seg_tree_find_gcd(i+1,N-1))
    ans=max(ans,ddd)
print(ans)