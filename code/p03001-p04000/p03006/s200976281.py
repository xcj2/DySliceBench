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
    self.root = [-1]*(n) #元々はn+1になっていたが、nに直した
    # 木をくっつける時にアンバランスにならないように調整する
    self.rnk = [0]*(n) #元々はn+1になっていたが、nに直した

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
    # すでに同じ木に属していた場合、何もしないで返す
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

  # ノードxが属する木のサイズを返す（根ノードの.root[idx]を-符号を外して返すだけ
  def Count(self, x):
    return -self.root[self.Find_Root(x)] #-符号を外す

  # 木の数（＝集合の数）を返す（根の数=rootに-符号を持つものの数を返すだけ）
  def Count_Trees(self):
    treecnt = 0
    for eachroot in self.root:
      if eachroot < 0: treecnt += 1
    return treecnt
#------Union-Findおわり-------------#

import collections

N = int(input())
XYs = [tuple(mi()) for _ in range(N)]

if N==1:
  print(1)
  exit()
if N==2:
  print(1)
  exit()

sa_list = []
cmb_with_same_diff = collections.defaultdict(list)
import itertools
diffidx = 0
for a in range(0, N):
  for b in range(0, N):
    if a>=b: continue
    #ここでa, bは各ボールのidx
    ax, ay = XYs[a]
    bx, by = XYs[b]
    if ax-bx==0: nowsa = (ax-bx,abs(ay-by))
    elif ay-by==0: nowsa = (abs(ax-bx), ay-by)
    elif ax-bx>0: nowsa = (ax-bx,ay-by)
    else: nowsa = (-(ax-bx),-(ay-by))
    sa_list.append(nowsa)
    cmb_with_same_diff[nowsa].append((a, b))

#print(sa_list)
#print(cmb_with_same_diff)

#最も多い差の個数（これ-1を短縮できるはず）
print(N-collections.Counter(sa_list).most_common()[0][1])

#[((x, y), 回数), ...]　多い順で入っている
#sa_sorted = collections.Counter(sa_list).most_common()

ans = N
for each_samesa_list in cmb_with_same_diff.values():
  UF = UnionFind(N) #ノード数はボールの数
#  print(each_samesa_list, 'における処理前の木の数は', UF.Count_Trees())
  for a, b in each_samesa_list:
    UF.Unite(a, b)
#  print(each_samesa_list, 'における処理後の木の数は', UF.Count_Trees())
  ans = min(ans, UF.Count_Trees())

#print(ans)

