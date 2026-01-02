import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
# template

# dfsの様々な実装例 in Python
# https://qiita.com/drken/items/a803d4fc4a727e02f7ba
# BEGIN CUT HERE


# v : 現在探索中の頂点，p : vの親（v が親のときは -1）
def dfs_tree(G,v,p):
    '''木上のdfsの実装例'''
    for nv in G[v]:
        if nv == p:
            continue
        dfs_tree(G, nv, v)
def main1():
    N = ii()
    G = [[] for i in range(N)]
    for i in range(N - 1):
        a, b = mi()
        G[a].append(b)
        G[b].append(a)
    
    root = 0
    dfs_tree(G, root, -1)

# 0を頂点とした木の根からの深さ，各頂点を根とした部分木のサイズを求める
# さっきのやつからすこし改造する
depth = [0] * (10 ** 5 + 10)
subtree_size = [0] * (10 ** 5 + 10)
# d : 頂点 v の深さ
def dfs_tree_kai(G, v, p, d):
    
    depth[v] = d
    for nv in G[v]:
        if nv == p:
            continue
        else:
            dfs_tree_kai(G, nv, v, d + 1)
    
    # 帰りがけ時に，部分木のサイズを求める
    subtree_size[v] = 1  # 自分自身
    for c in G[v]:
        if c == p:
            continue
        subtree_size[v] += subtree_size[c]
    return depth, subtree_size

def main2():
    '''木DPの簡単な例（部分木のサイズを求める）'''
    N = ii()
    G = [[] for i in range(N)]
    for i in range(N - 1):
        a, b = mi()
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    
    root = 0  # 仮に頂点0を根とする
    dfs_tree_kai(G, root, -1, 0)
    
    for v in range(N):
        print(v, ": depth = ", depth[v], ", subtree_size = ", subtree_size[v])
    
def EDPC_P():
    N = ii()
    dp = [[1, 1] for _ in range(N)]
    G = [[] for i in range(N)]
    for i in range(N - 1):
        a, b = mi()
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    depth = [0]*N
    def dfs_EDPC_P(G, v, p, d):
        depth[v] = d
        for nv in G[v]:
            if nv == p:
                continue
            dfs_EDPC_P(G, nv, v, d + 1)
        for c in G[v]:
            if c == p:
                continue
            dp[v][0] *= (dp[c][0] + dp[c][1]) % (10 ** 9 + 7)
            dp[v][1] *= dp[c][0]
    dfs_EDPC_P(G,0,-1,0)
    print((dp[0][0]+dp[0][1])%(10**9+7))
    
# END CUT HERE

if __name__ == '__main__':
    EDPC_P()