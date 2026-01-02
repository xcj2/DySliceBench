import sys
input = sys.stdin.readline

N,M=map(int,input().split())

end=[[] for i in range(N+2)]

for i in [0]*M:
    l,r,a=map(int,input().split())
    end[r+1].append((l,a))

#Starry Sky tree
seg_el=1<<18#Segment treeの台の要素数

SEG=[0]*(2*seg_el-1)#Segment tree.色々考えると0で初期化してOKそう
ADD=[0]*(2*seg_el-1)#加算用Segment tree,SEG[k]+ADD[k]がkにおける本当の最大値
seg_el_list=[524286, 262142, 131070, 65534, 32766, 16382, 8190, 4094, 2046, 1022, 510, 254, 126, 62, 30, 14, 6, 2, 0]

def update(k):#SEGのkより上のノードを更新（反映）
    while k>=0:
        k=(k-1)//2
        if SEG[k]==max(SEG[k*2+1]+ADD[k*2+1],SEG[k*2+2]+ADD[k*2+2]):
            break
        SEG[k]=max(SEG[k*2+1]+ADD[k*2+1],SEG[k*2+2]+ADD[k*2+2])

def to_seg(a):#aが終点となる区間をSegment treeの座標へ変換  
    b=(a&(-a)).bit_length()
    return seg_el_list[b]+a//(1<<(b-1))

def add(a,b,x):#区間(a,b]にxを加算
    #print(a,b,x)
    while b!=0:
        ADD[to_seg(b)]+=x
        update(to_seg(b))
        b-=(b&(-b))

    while a!=0:
        ADD[to_seg(a)]+=-x
        update(to_seg(a))
        a-=(a&(-a))
    
for i in range(N+2):
    for b,k in end[i]:
        add(b,i,k)#点数がもらえる区間から出たときにその分を加算

    SEG[i+seg_el-1]=SEG[0]
    update(i+seg_el-1)

print(SEG[0])