def makelist(n, m):
    return [[0 for _ in range(m)] for _ in range(n)]


N, M = map(int, input().split())
A = [0]*(M+1)
B = [0]*(M+1)
for i in range(1, M+1):
    A[i], B[i] = map(int, input().split())


##
v = N+1
uni = [-1]*v  # 根であれば *そのグループの要素数(負)* が、子であれば親の番号が入る。
              # 初期値に -1 を入れておく
              # v は頂点数

# 頂点 v の所属するグループを調べる
def root(v):
    if uni[v] < 0:  # v が親の場合
        return v
    else:           # v が子の場合
        uni[v] = root(uni[v])  # 親のrootを調べる
        return uni[v]

# 頂点 a と頂点 b をつなぐ。もともと同じグループのとき、False を返す
def connect(a, b):
    # まずはそれぞれ根の番号に置き換える
    ra = root(a)
    rb = root(b)
    if ra == rb:  # a と b がそもそも同じグループに属しているなら即終了
        return False
    
    # ra を大きなグループにしたいので、逆であれば入れ替える
    if uni[ra] > uni[rb]: # rbの方が要素数が多ければ
        ra, rb = rb, ra

    # ra と rb を結合し、rb の親を ra とする
    uni[ra] += uni[rb]
    uni[rb] = ra
    return True

# 頂点 a, b が同じグループであるかを調べる
def isConnect(a, b):
    return root(a) == root(b)

# 頂点 a を含むグループの頂点数を調べる
def size(a):
    return -uni[root(a)]


base = (N * (N-1)) // 2
bene = 0
ans = [base]
for i in reversed(range(2, M+1)):
    a, b = A[i], B[i]

    if not isConnect(a, b):
        bene += size(a) * size(b)
        connect(a, b)
    ans.append(base-bene)

for e in reversed(ans):
    print(e)
