from collections import deque
import sys
sys.setrecursionlimit(10**9 + 7)


def dfs1(pos, par, e=1):
    """dfsを用いて前計算する"""
    for child in tree[pos]:
        if child == par:
            continue
        tmp = st_val[child]
        e *= (1 + tmp)
        e %= MOD
    st_val[pos] = e
    return st_val[pos]


def dfs2(pos, par, e=1):
    """全方位木DP"""
    for child in tree[pos]:
        if child == par:
            ind = compress[par][pos]
            tmp = ruiseki_l[par][ind] * ruiseki_r[par][len(tree[par]) - ind - 1]
        else:
            tmp = st_val[child]
        e *= (1 + tmp)
        e %= MOD
        ind = compress[pos][child]
        re_subtree_val[pos][ind] = 1 + tmp

    for i in range(len(tree[pos])):
        ruiseki_l[pos][i + 1] = ruiseki_l[pos][i] * re_subtree_val[pos][i]
        ruiseki_l[pos][i + 1] %= MOD
    for i in range(len(tree[pos])):
        ruiseki_r[pos][i + 1] = ruiseki_r[pos][i] * re_subtree_val[pos][-i-1]
        ruiseki_r[pos][i + 1] %= MOD
    ans[pos] = e



def topological_sort(root, par=-1):
    q = deque([(root, par)])
    res = [(root, par)]
    while q:
        pos, par = q.pop()
        for child in tree[pos]:
            if child == par:
                continue
            else:
                q.append((child, pos))
                res.append((child, pos))
    return res


n, m = map(int, input().split())
MOD = m
info = [list(map(int, input().split())) for i in range(n-1)]
tree = [[] for i in range(n)]
for i in range(n-1):
    a, b = info[i]
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)

# 木上のdfsの行きがけ順
preorder_list = topological_sort(0, par=-1)

# subtreeから値を集める
st_val = [0] * n
for pos, par in reversed(preorder_list):
    dfs1(pos, par)

# rerootによって、subtreeから値を集める。
re_subtree_val = [[1] * len(tree[i]) for i in range(n)]

# 左右それぞれの累積
ruiseki_l = [[1] * (len(tree[i]) + 1) for i in range(n)]
ruiseki_r = [[1] * (len(tree[i]) + 1) for i in range(n)]

compress = [{v: j for j, v in enumerate(tree[i])} for i in range(n)]
ans = [0]*n
for pos, par in preorder_list:
    dfs2(pos, par)

for i in range(n):
    print(ans[i] % MOD)

