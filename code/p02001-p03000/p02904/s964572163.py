import sys
input = sys.stdin.readline

N,K=map(int,input().split())
A=list(map(int,input().split()))

# Segment tree(1-indexed,再帰を使わないもの,最小値を求める)

seg_el=1<<(N.bit_length())# Segment treeの台の要素数
SEG=[1<<30]*(2*seg_el)# 1-indexedなので、要素数2*seg_el.Segment treeの初期値で初期化

for i in range(N):# Aを対応する箇所へupdate
    SEG[i+seg_el]=A[i]

for i in range(seg_el-1,0,-1):# 親の部分もupdate
    SEG[i]=min(SEG[i*2],SEG[i*2+1])

def update(n,x,seg_el):# A[n]をxへ更新（反映）
    i=n+seg_el
    SEG[i]=x
    i>>=1# 子ノードへ
    
    while i!=0:
        SEG[i]=min(SEG[i*2],SEG[i*2+1])
        i>>=1
        
def getvalues(l,r):# 区間[l,r)に関するminを調べる
    L=l+seg_el
    R=r+seg_el
    ANS=1<<30

    while L<R:
        if L & 1:
            ANS=min(ANS , SEG[L])
            L+=1

        if R & 1:
            R-=1
            ANS=min(ANS , SEG[R])
        L>>=1
        R>>=1

    return ANS

SEG2=[1<<30]*(2*seg_el)# 1-indexedなので、要素数2*seg_el.Segment treeの初期値で初期化

for i in range(N):# Aを対応する箇所へupdate
    SEG2[i+seg_el]=A[i]

for i in range(seg_el-1,0,-1):# 親の部分もupdate
    SEG2[i]=max(SEG2[i*2],SEG2[i*2+1])

def update2(n,x,seg_el):# A[n]をxへ更新（反映）
    i=n+seg_el
    SEG2[i]=x
    i>>=1# 子ノードへ
    
    while i!=0:
        SEG2[i]=max(SEG2[i*2],SEG2[i*2+1])
        i>>=1
        
def getvalues2(l,r):# 区間[l,r)に関するmaxを調べる
    L=l+seg_el
    R=r+seg_el
    ANS=-1

    while L<R:
        if L & 1:
            ANS=max(ANS , SEG2[L])
            L+=1

        if R & 1:
            R-=1
            ANS=max(ANS , SEG2[R])
        L>>=1
        R>>=1

    return ANS

# UnionFind

Group=[i for i in range(N-K+1)]# グループ分け.Group[i]=jのときiとjは同じグループ

def find(x):# find(a)=find(b)のとき同じグループ
    if Group[x]==-1:
        return -1
    
    while Group[x] != x:
        x=Group[x]
    return x

def Union(x,y):  # xとyが同じグループになるよう更新
    if find(x) != find(y):
        Group[find(y)]=Group[find(x)]=min(find(y),find(x))

count=0
for i in range(1,N):
    if A[i]>A[i-1]:
        count+=1
    else:
        count=0
    if count>=K-1:
        Group[i-K+1]=-1
    

for i in range(N-K):
    if A[i]<getvalues(i+1,i+K)<getvalues2(i+1,i+K)<A[i+K]:
        Union(i,i+1)

B=[find(x) for x in range(N-K+1)]
#print(B)
print(len(set(B)))
