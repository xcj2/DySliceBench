import sys
input = sys.stdin.readline

N,Q=map(int,input().split())

seg_el=1<<((N+1).bit_length()) # Segment treeの台の要素数

SEG=[N-2]*(2*seg_el) # 1-indexedなので、要素数2*seg_el.Segment treeの初期値で初期化
SEG2=[N-2]*(2*seg_el)

def getvalue(n,seg_el): # 一点の値を取得
    i=n+seg_el
    ANS=N-2
    
    ANS=min(SEG[i],ANS)
    i>>=1# 子ノードへ
    
    while i!=0:
        ANS=min(SEG[i],ANS)
        i>>=1

    return ANS

def getvalue2(n,seg_el): # 一点の値を取得
    i=n+seg_el
    ANS=N-2
    
    ANS=min(SEG2[i],ANS)
    i>>=1# 子ノードへ
    
    while i!=0:
        ANS=min(SEG2[i],ANS)
        i>>=1

    return ANS

def updates(l,r,x): # 区間[l,r)のminを更新.
    L=l+seg_el
    R=r+seg_el

    while L<R:
        if L & 1:
            SEG[L]=min(x,SEG[L])
            L+=1

        if R & 1:
            R-=1
            SEG[R]=min(x,SEG[R])
        L>>=1
        R>>=1

def updates2(l,r,x): # 区間[l,r)のminを更新.
    L=l+seg_el
    R=r+seg_el

    while L<R:
        if L & 1:
            SEG2[L]=min(x,SEG2[L])
            L+=1

        if R & 1:
            R-=1
            SEG2[R]=min(x,SEG2[R])
        L>>=1
        R>>=1

ANS=(N-2)*(N-2)

MINX=N
MINY=N

for queries in range(Q):
    t,x=map(int,input().split())

    if t==1:
        v=getvalue(x,seg_el)
        ANS-=v
        updates2(1,MINY,x-2)
        MINX=min(MINX,x)

    else:
        v=getvalue2(x,seg_el)
        ANS-=v
        updates(1,MINX,x-2)
        MINY=min(MINY,x)

print(ANS)
        
        

    

