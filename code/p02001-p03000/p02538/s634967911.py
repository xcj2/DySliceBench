import sys
input = sys.stdin.readline

N,Q=map(int,input().split())

mod=998244353

seg_el=1<<(N.bit_length()) # Segment treeの台の要素数
seg_height=1+N.bit_length() # Segment treeの高さ
SEG=[0 for i in range(2*seg_el)] # 区間の和
LAZY=[0 for i in range(2*seg_el)]


POW10=[1]
for i in range(N+1):
    POW10.append(POW10[-1]*10%mod)

gyaku=pow(9,mod-2,mod)

def seg_function(x,y):
    return (x+y)%mod
    
for i in range(N): # Aを対応する箇所へupdate
    SEG[i+seg_el]=POW10[i]
        
for i in range(seg_el-1,0,-1): # 親の部分もupdate
    SEG[i]=seg_function(SEG[i*2],SEG[i*2+1])

def lazy_change(ind,b):
    kousuu = 1<< (seg_height - (ind.bit_length()))
    tyousei = (ind - (1<<((ind.bit_length())-1)))*kousuu

    #print(ind,tyousei,kousuu)
    SEG[ind] = POW10[tyousei] * b * (POW10[kousuu]-1) %mod * gyaku %mod

def lazy_compose(ind,b):
    LAZY[ind]=b

def indexes(L,R): # 遅延伝搬すべきノードのリストを下から上の順に返す. （つまり, updateやgetvaluesで見るノードより上にあるノードたち）
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
        

def changes(l,r,b0): # 区間[l,r)更新
        
    L=l+seg_el
    R=r+seg_el

    L//=(L & (-L))
    R//=(R & (-R))

    UPIND=indexes(L,R)
    
    for ind in UPIND[::-1]:
        if LAZY[ind]!=0:
            b=LAZY[ind]
            
            lazy_change(ind<<1,b)
            lazy_change(1+(ind<<1),b)
            
            lazy_compose(ind<<1,b)
            lazy_compose(1+(ind<<1),b)
            
            LAZY[ind]=0

    #print(SEG)
    
    while L!=R:
        if L > R:
            lazy_change(L,b0)
            lazy_compose(L,b0)
            L+=1
            L//=(L & (-L))

        else:
            R-=1
            lazy_change(R,b0)
            lazy_compose(R,b0)
            R//=(R & (-R))

    for ind in UPIND:
        SEG[ind]=seg_function(SEG[ind<<1],SEG[1+(ind<<1)])
    

for qu in range(Q):
    L,R,D=map(int,input().split())
    L,R=N-R+1,N-L+1
    #print(SEG)

    changes(L-1,R,D)
    sys.stdout.write(str(SEG[1])+"\n")
