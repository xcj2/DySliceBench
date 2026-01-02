###template###
import sys
def input(): return sys.stdin.readline().rstrip()
def mi(): return map(int, input().split())
###template###

#Union-Find ****0スタートなので注意！****
class UnionFind():
    # 作りたい要素数（ノードの数）nで初期化
    # 使用するインスタンス変数の初期化
    def __init__(self, n):
        self.n = n
        # root[x]<0ならそのノードが根かつその値が木の要素数
        # rootノードでその木の要素数を記録する
        self.root = [-1]*(n+1)
        # 木をくっつける時にアンバランスにならないように調整する
        self.rnk = [0]*(n+1)

    # ノードxのrootノードを見つける
    def Find_Root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            # ついでに経路圧縮（調べた辺を根に直接つなぎ直す）をかけておく
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]
    # 木の併合、入力は併合したい集合に属する各ノード
    def Unite(self, x, y):
        # 入力ノードのrootノードを見つける
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        # すでに同じ木に属していた場合
        if(x == y):
            return
        # 違う木に属していた場合rnkを見てくっつける方を決める
        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y] #要素数を足す(根のrootは"-要素数")
            self.root[y] = x #ノードyの親をx（新しい集合の根）とする
        else:
            self.root[y] += self.root[x] #要素数を足す
            self.root[x] = y
            # rnkが同じ（深さに差がない場合）は1増やす（根(rnk1)+繋げる集合のrnkということで、1増えることになる）
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1
    # xとyが同じグループに属するか判断
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    # ノードxが属する木のサイズを返す
    def Count(self, x):
        return -self.root[self.Find_Root(x)] #-符号を外す

#組み合わせ計算
cmbDP = [-1]*500002 #組み合わせDP用
def cmb(n, r):
    global cmbDP
    if cmbDP[n]+1: return cmbDP[n] #計算済みなら
    if n - r < r: r = n - r
#    if r == 0: return 1
#    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    cmbDP[n] = result
    return result


N, M = mi()
ABs = [list(mi()) for _ in range(M)][::-1]

#UnionFind用のインスタンスを要素数Mで作成(0スタート)
UFNodes = UnionFind(M)

#橋が全て崩落した場合の不便さから順（逆順）に答えを入れていく
nowans = cmb(N, 2) #全ての島の組み合わせ数=全て崩落した場合の不便さ
anslist = [nowans,]
#ここからは、nowans-=新しく繋がった島の組み合わせ数（橋が復旧した場合の便利さ）で要素を足していく
#最後の一つは、「全て復旧した場合」＝初期状態ということで、出力対象外なので注意

for a, b in ABs:
  #0スタートに変える
  a, b = a-1, b-1
  if UFNodes.isSameGroup(a, b): #既に同じ木なら、行き来可能状況に変化は起きないので、同じansを再度入れればいいだけ
    anslist.append(nowans)
  else: #違う場合、uniteすることになるが、unite前の要素数が欲しい
    prevacnt = UFNodes.Count(a)
    prevbcnt = UFNodes.Count(b)
    UFNodes.Unite(a,b)
    nowans -= prevacnt * prevbcnt
    anslist.append(nowans)


for eachans in anslist[:-1][::-1]:
  print(eachans)
