import heapq
import math
def set_heapq(que, edge, used, v, add_dist=0):
    '''
    確定地点vからつながる辺を全てqueに設定し、返却する

    Parameters
    que : heapque(touple or list)
        辺を管理するキュー (距離、次の行き先)のtopuleまたはlistにて管理
    edge : list
        全ての辺を格納する二次元のリスト edge[0]にてノード0から伸びる辺であることを表し、
        edge[0] → [距離、次の行き先] を表すlistが格納されている
    v : int
        グラフ上のノード ダイクストラでは確定したノードがvにあたる
    add_dist : int
        確定した地点に足し合わせる距離 スタート地点以外では何かしらの値が追加されることになる

    Returns
    que : heapque(touple or list)
        引数queにvからつながる辺を追加したキュー
    '''
    for a,b in edge[v]:
        if used[b]:
            heapq.heappush(que,(a+add_dist,b))
    return que

def prim_heap(edge, n):
    '''
    プリム法で最小全域木を求める

    Parameters
    edge : list
        全ての辺を格納する二次元のリスト edge[0]にてノード0から伸びる辺であることを表し、
        edge[0] → [距離、次の行き先] を表すlistが格納されている
    
    Returns
    res : int
        最小全域木の全ての辺のコストの総和
    '''
    used = [True] * n #True:不使用
    edgelist = []
    edgelist = set_heapq(edgelist, edge, used, 0)
    used[0] = False
    res = 0
    while len(edgelist) != 0:
        minedge = heapq.heappop(edgelist)
        if not used[minedge[1]]:
            continue
        v = minedge[1]
        used[v] = False
        edgelist = set_heapq(edgelist, edge, used, v)
        res += minedge[0]
    return res

def write_file(s):
    with open("tmp.txt", "a") as f:
        f.write(s+"\n")

while True:
    N = int(input())
    if N == 0: break
    xyzr = [list(map(float, input().split())) for _ in range(N)]
    edge = [[] for _ in range(N)]
    # 全ての組み合わせを列挙して、距離を求める
    for i in range(N):
        for j in range(i+1,N):
            x1,y1,z1,r1 = xyzr[i]
            x2,y2,z2,r2 = xyzr[j]
            dist = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z1-z2)**2)
            dist = max(0, dist-r1-r2)
            edge[i].append((dist, j))
            edge[j].append((dist, i))
    ans = prim_heap(edge, N)
    ans = ('{:0.3f}'.format(ans))
    print(ans)

