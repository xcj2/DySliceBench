import sys
input = sys.stdin.readline

N=int(input())
LR=[tuple(map(int,input().split())) for i in range(N)]

LR.sort()

# Segment tree(1-indexed,再帰を使わないもの,最小値を求める)

seg_el=1<<(N.bit_length())# Segment treeの台の要素数
SEG=[1<<30]*(2*seg_el)# 1-indexedなので、要素数2*seg_el.Segment treeの初期値で初期化

for i in range(N):# Aを対応する箇所へupdate. Aは0-indexedなことに注意. 
    SEG[i+seg_el]=LR[i][1]

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

SEG2=[-1]*(2*seg_el)# 1-indexedなので、要素数2*seg_el.Segment treeの初期値で初期化

for i in range(N):# Aを対応する箇所へupdate. Aは0-indexedなことに注意. 
    SEG2[i+seg_el]=LR[i][0]

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

ANS=0

for i in range(N):
    ANS=max(ANS,LR[i][1]-LR[i][0]+1+max(0,min(getvalues(0,i),getvalues(i+1,N))-max(getvalues2(0,i),getvalues2(i+1,N))+1))

    #print(LR[i][1]-LR[i][0]+1+max(0,min(getvalues(0,i),getvalues(i+1,N))-max(getvalues2(0,i),getvalues2(i+1,N))+1))

LR2=[LR[0]]

for i in range(N):
    if LR[i][0]==LR2[-1][0]:
        continue
    while len(LR2)>0 and LR2[-1][0]<=LR[i][0] and LR2[-1][1]>=LR[i][1]:
        LR2.pop()

    LR2.append(LR[i])

LN=len(LR2)

SEG=[1<<30]*(2*seg_el)# 1-indexedなので、要素数2*seg_el.Segment treeの初期値で初期化

for i in range(LN):# Aを対応する箇所へupdate. Aは0-indexedなことに注意. 
    SEG[i+seg_el]=LR2[i][1]

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

SEG2=[-1]*(2*seg_el)# 1-indexedなので、要素数2*seg_el.Segment treeの初期値で初期化

for i in range(LN):# Aを対応する箇所へupdate. Aは0-indexedなことに注意. 
    SEG2[i+seg_el]=LR2[i][0]

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


for i in range(1,LN):
    ANS=max(ANS,max(0,getvalues(0,i)-getvalues2(0,i)+1)+max(0,getvalues(i,LN)-getvalues2(i,LN)+1))

    #print(max(0,getvalues(0,i)-getvalues2(0,i)+1))
    #print(max(0,getvalues(i,LN)-getvalues2(i,LN)+1))

print(ANS)