
"""
Writer: SPD_9X2
https://atcoder.jp/contests/dp/tasks/dp_q
いわゆるインラインdpなのは分かった
→どこが？

dpを決めると、更新式がセグ木などで更新可能？
dp[i][h] = i番目まで見て、最大の高さがhの時の美しさの総和の最大値

dp[i][h] = max( dp[i-1][0] , dp[i-1][1] , … , dp[i-1][h-1] ) + a[i]
なので,RMQで処理できる
→これがインラインdpなのか？？

"""

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
        tree[i] = max(tree[i * 2 + 2] , tree[i * 2 + 1])

    return

def RMQ_query(a,b,k,l,r,tree): #query区間左,右,注目ノード番号,担当範囲左,担当範囲右,木

    if r <= a or b <= l: #区間が完全にかぶらない場合inf
        return 0
    
    if a <= l and r <= b: #区間が完全に含まれる場合自分
        return tree[k]

    c1 = RMQ_query(a,b,2*k+1,l,(l+r)//2,tree)
    c2 = RMQ_query(a,b,2*k+2,(l+r)//2,r,tree)   

    return max(c1,c2)


N = int(input())
h = list(map(int,input().split()))
a = list(map(int,input().split()))

tree = make_ST(N+1,0)

for i in range(N):

    maxi_sc = RMQ_query(0,h[i],0,0,(len(tree)+1)//2,tree)
    RMQ_update_point(maxi_sc+a[i] , h[i] ,tree)

print (RMQ_query(0,N+1,0,0,(len(tree)+1)//2,tree))

