from sys import stdin
import heapq

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
        return (float("inf"),float("inf"))
    
    if a <= l and r <= b: #区間が完全に含まれる場合自分
        return tree[k]

    c1 = RMQ_query(a,b,2*k+1,l,(l+r)//2,tree)
    c2 = RMQ_query(a,b,2*k+2,(l+r)//2,r,tree)   

    return min(c1,c2)
        

def want(L,R):

    if L >= R:
        return
    elif L + 1 == R:
        heapq.heappush( q, (p[L],p[R],float("inf"),float("-inf"),float("inf"),float("-inf")) )
        return

    if L % 2 == 0:
        nx,xind = RMQ_query(L,R+1,0,0,(len(emin)+1)//2,emin)
        ny,yind = RMQ_query(xind+1,R+1,0,0,(len(omin)+1)//2,omin)
    else:
        nx,xind = RMQ_query(L,R+1,0,0,(len(omin)+1)//2,omin)
        ny,yind = RMQ_query(xind+1,R+1,0,0,(len(emin)+1)//2,emin)

    #print (L,R,xind,yind)

    heapq.heappush( q , (nx,ny,xind,yind,L,R) )
    return

N = int(input())
p = list(map(int, stdin.readline().split()))


omin = make_ST(N, (float("inf") , float("inf")) )
emin = make_ST(N, (float("inf") , float("inf")) )

for i in range(N):
    if i % 2 == 0:
        RMQ_update_point( (p[i],i) ,i,emin)
    else:
        RMQ_update_point( (p[i],i) ,i,omin)

q = []
want(0,N-1)
ans = []

while len(q) > 0:

    x,y,xi,yi,NL,NR = heapq.heappop(q)
    ans.append(x)
    ans.append(y)

    want(NL,xi-1)
    want(xi+1,yi-1)
    want(yi+1,NR)

print (*ans)

