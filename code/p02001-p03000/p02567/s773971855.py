import sys
input = sys.stdin.readline

N,Q=map(int,input().split())
A=list(map(int,input().split()))

seg_el=1<<(N.bit_length()) # Segment treeの台の要素数
SEG=[0]*(2*seg_el) # 1-indexedなので、要素数2*seg_el.Segment treeの初期値で初期化

for i in range(N): # Aを対応する箇所へupdate. Aは0-indexedなことに注意. 
    SEG[i+seg_el]=A[i]

for i in range(seg_el-1,0,-1): # 親の部分もupdate
    SEG[i]=max(SEG[i*2],SEG[i*2+1])

def update(n,x,seg_el): # A[n]をxへ更新（反映）
    i=n+seg_el
    SEG[i]=x
    i>>=1 # 子ノードへ
    
    while i!=0:
        SEG[i]=max(SEG[i*2],SEG[i*2+1])
        i>>=1
        
def getvalues(l,r): # 区間[l,r)に関するmaxを調べる
    L=l+seg_el
    R=r+seg_el
    ANS=0

    while L<R:
        if L & 1:
            ANS=max(ANS , SEG[L])
            L+=1

        if R & 1:
            R-=1
            ANS=max(ANS , SEG[R])
        L>>=1
        R>>=1

    return ANS

def bisect_on_SEG(l,x):  
    L=l+seg_el
    R=seg_el*2-1
    while L<R:
        if SEG[L]>=x:
            break
        if L & 1:
            L+=1
        L>>=1
        R>>=1

    if SEG[L]<x:
        return N

    while L<seg_el:
        if SEG[L*2]>=x:
            L=L*2
        else:
            L=L*2+1

    return L-seg_el

for queries in range(Q):
    T,X,V=map(int,input().split())
    if T==1:
        update(X-1,V,seg_el)
    elif T==2:
        print(getvalues(X-1,V))
    else:
        print(1+bisect_on_SEG(X-1,V))