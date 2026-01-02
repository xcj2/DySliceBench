
def make_ST(n,first): #firstで初期化された、葉がn要素を超えるように2のべき乗個用意されたリストを返す

    i = 0
    ret = []
    while 2 ** (i-1) < n:

        for j in range(2 ** i):
            ret.append(first)

        i += 1

    return ret

def RMQ_update_point(num,point,tree): #葉のindex(0-origin)がpointの要素をnumにする/treeはセグ木

    i = (len(tree) - 1) // 2 + point
    tree[i] = num
    while i > 0:
        i = (i - 1) // 2
        tree[i] = min(tree[i * 2 + 2] , tree[i * 2 + 1])

    return

def RMQ_query(a,b,k,l,r,tree): #query区間左,右,注目ノード番号,担当範囲左,担当範囲右,木

    if r <= a or b <= l: #区間が完全にかぶらない場合inf
        return float("inf")
    
    if a <= l and r <= b: #区間が完全に含まれる場合自分
        return tree[k]

    c1 = RMQ_query(a,b,2*k+1,l,(l+r)//2,tree)
    c2 = RMQ_query(a,b,2*k+2,(l+r)//2,r,tree)   

    return min(c1,c2)
        

n,q = map(int,input().split())

ABLE_MAX = 2 ** 31 - 1
segt = make_ST(n,ABLE_MAX)

for i in range(q):

    com,x,y = map(int,input().split())

    if com == 0:
        RMQ_update_point(y,x,segt)
    else:
        print (RMQ_query(min(x,y+1),max(x,y+1),0,0,(len(segt)+1)//2,segt))

