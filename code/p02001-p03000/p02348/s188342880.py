n,q=map(int,input().split())
Q=[list(map(int,input().split())) for i in range(q)]


for i in range(30):#要素数以上の2のベキを見つける
    if n<=1<<i:
        seg_el=1<<i#Segment treeの台の要素数
        break

SEG=[None for i in range(2*seg_el-1)]#Segment tree（遅延伝搬を用いるが、一本のセグ木でOK）

def lazy_update(k,x):#一つ下の子へ伝搬
    if 0<=k<seg_el-1:
        lazy_item,SEG[k]=SEG[k],None
        SEG[k*2+1]=SEG[k*2+2]=lazy_item


def update(a,b,x,k,l,r):
    if SEG[k]!=None:#アクセスした箇所にデータが入っていたときは,評価を伝搬させる
        lazy_update(k,x)
        
    if r<=a or b<=l:#区間[a,b)が対象区間の外にあれば終了
        return 
    if a<=l and r<=b:#区間[a,b)が対象区間の中にあればSEG[k]を更新.後にアクセスされたときに遅延評価する.
        SEG[k]=x#
        return 
    update(a,b,x,k*2+1,l,(l+r)//2)#それ以外のときは,SEG[k*2+1]とSEG[k*2+2]で場合分け
    update(a,b,x,k*2+2,(l+r)//2,r)

def getvalue(n):#値を得る
    i=n+seg_el-1
    ANS=SEG[i]
    i=(i-1)//2

    while i>=0:
        if SEG[i]!=None:
            ANS=SEG[i]#できるだけ親に近いノードから値を得るようにする.（そこが最後に更新されたものなので）
        i=(i-1)//2
    return ANS

for i in range(n):
    SEG[i+seg_el-1]=(1<<31)-1

for query in Q:
    if query[0]==0:
        update(query[1],query[2]+1,query[3],0,0,seg_el)
    else:
        print(getvalue(query[1]))

