import sys
sys.setrecursionlimit(100000)

# Union-Findの用意
def root(x):
    '''島xの根を求める'''
    if par[x] == x:
        return x
    else:
        par[x] = root(par[x])
        return root(par[x])
    
def same(x, y):
    return root(x) == root(y)

def unite(x, y):
    '''2つの島の根をつなぎ、島のサイズを更新する'''
    x = root(x)
    y = root(y)
    if x == y:
        return

    par[x] = y
    size[y] = size[x] + size[y]

# 初期値の入力
n, m = [int(x) for x in input().split()]
A = [[int(x)-1 for x in input().split()] for i in range(m)]

# N個の島(0, 1, ..., n-1)がある
#N = [i for i in range(n)]
# それぞれの島の「根」と、その根に属する島の数を更新していく
par = [i for i in range(n)]
size = [1] * n

# 逆順につないでいく
# 不便さは、数列的な考えでいく。初期値は
ans = [0] * m
ans[m-1] = n * (n-1) // 2

for i in reversed(range(m-1)):
    n1 = size[root(A[i+1][0])]
    n2 = size[root(A[i+1][1])]

    if same(A[i+1][0], A[i+1][1]):
        ans[i] = ans[i+1]
    else:
        ans[i] = ans[i+1] - n1 * n2

    unite(A[i+1][0], A[i+1][1])

for i in ans:
    print(i)

# 一本つないだとき、別のグループ同士がつながれば、その組み合わせ分不便さが減る
# Union-Findの実装は定型ではなく、応用が幅広い
# 1~Nの島があり、1本ずつつないでいく
# 知りたいのは、各頂点がどのグループに所属し、そのグループのメンバーの個数はいくつか、ということ
