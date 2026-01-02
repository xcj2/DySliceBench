import math
inf=0
def segtree(a): #RMQ(Range Minimum Query)
    #bi=高さ　bi2=最下段の個数
    global bi 
    bi=math.ceil(math.log2(len(a)))+1
    global bi2
    bi2=2**(bi-1)
    seg=[inf]*(2*bi2-1)
    for i in range(len(a)):
        seg[bi2+i-1]=a[i]
    for i in range(bi-1):
        for j in range(2**(bi-i-2)):
            b=2**(bi-i-2)-1+j
            seg[b]=math.gcd(seg[2*b+1],seg[2*b+2])
    return seg

def seg_update(loc,val): #locの値をvalueに更新
    loc+=bi2-1
    seg[loc]=val
    while True:
        seg[loc]=math.gcd(val,seg[loc])
        if loc==0:
            break
        loc=(loc-1)//2

def seg_find(l,r,tmp=0): #[l,r)の最小値を求める
    a=bi-math.ceil(math.log2(tmp+2))+1
    nl=2**(a-1)*(tmp-(2**(bi-a))+1)
    nr=nl+2**(a-1)
    if nr<=l or nl>=r:
        return inf
    elif l<=nl and nr<=r:
        return seg[tmp]
    else:
        return math.gcd(seg_find(l,r,tmp*2+1),seg_find(l,r,tmp*2+2))

n=int(input())
seg=segtree(list(map(int,input().split())))
ans=0
for i in range(n):
    ans=max(ans,math.gcd(seg_find(0,i),seg_find(i+1,n)))
print(ans)