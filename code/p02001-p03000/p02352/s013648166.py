import sys
input = sys.stdin.readline

N,Q=map(int,input().split())

seg_el=1<<(N.bit_length()) # Segment treeの台の要素数
SEG=[0]*(2*seg_el) # 1-indexedなので、要素数2*seg_el.Segment treeの初期値で初期化
LAZY=[0]*(2*seg_el) # 1-indexedなので、要素数2*seg_el.Segment treeの初期値で初期化

def indexes(L,R): # 遅延伝搬すべきノードのリストを返す. （つまり, updateやgetvaluesで見るノードより上にあるノードたち）
    INDLIST=[]

    R-=1
    
    L>>=1
    R>>=1

    while L!=R:
        if L>R:
            INDLIST.append(L)
            L>>=1
        else:
            INDLIST.append(R)
            R>>=1

    while L!=0:
        INDLIST.append(L)
        L>>=1

    return INDLIST
        

def adds(l,r,x): # 区間[l,r)を +x 更新
        
    L=l+seg_el
    R=r+seg_el

    L//=(L & (-L))
    R//=(R & (-R))

    UPIND=indexes(L,R)
    
    while L!=R:
        if L > R:
            SEG[L]+=x
            LAZY[L]+=x
            L+=1
            L//=(L & (-L))

        else:
            R-=1
            SEG[R]+=x
            LAZY[R]+=x
            R//=(R & (-R))

    for ind in UPIND:
        SEG[ind]=min(SEG[ind<<1],SEG[1+(ind<<1)])+LAZY[ind]
        
def getvalues(l,r): # 区間[l,r)に関するminを調べる

    L=l+seg_el
    R=r+seg_el

    L//=(L & (-L))
    R//=(R & (-R))

    UPIND=indexes(L,R)
    
    for ind in UPIND[::-1]: # 遅延伝搬
        if LAZY[ind]!=0:
            plus_lazy=LAZY[ind]
            
            SEG[ind<<1]+=plus_lazy
            SEG[1+(ind<<1)]+=plus_lazy
            
            LAZY[ind<<1]+=plus_lazy
            LAZY[1+(ind<<1)]+=plus_lazy
            
            LAZY[ind]=0
            
    ANS=1<<31

    while L!=R:
        if L > R:
            ANS=min(ANS , SEG[L])
            L+=1
            L//=(L & (-L))

        else:
            R-=1
            ANS=min(ANS , SEG[R])
            R//=(R & (-R))

    return ANS

ANS=[]

for _ in range(Q):
    query=list(map(int,input().split()))
    if query[0]==0:
        adds(query[1],query[2]+1,query[3])

    else:
        ANS.append(getvalues(query[1],query[2]+1))

print("\n".join([str(ans) for ans in ANS]))

