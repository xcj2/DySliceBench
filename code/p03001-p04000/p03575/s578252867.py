import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
sys.setrecursionlimit(10**7)
inf = 10 ** 20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def _I(): return int(sys.stdin.readline())
def _F(): return float(sys.stdin.readline())
def _pf(s): return print(s, flush=True)

N, M = LI()
A, B = [], []
for i in range(M):
    a, b = LI()
    A.append(a)
    B.append(b)

"""
頂点ごとにみる。
その頂点につながっている辺を洗い出す
洗い出した辺の頂点同士がつながっているか確認する
最終的に自分のもとに戻ってこれるか。
dfsで全経路を洗い出す
1とそれ以外が全部つながるか。
2とそれ以外が全部つながるかを調査すればよい
"""

#  def dfs(reached_nodes, lines):
#      print('df', reached_nodes, lines, file=sys.stderr)
#      # 最初に与えられた線からたどっていって、すべての線を洗い出す。すべての頂点が入っていればおK
#      # このノードにつながっている辺をみつける
#      for line in lines:
#          if line[0] in reached_nodes or line[1] in reached_nodes:
#              # 既に到達しているnodeに入っている場合
#              new_lines = [l for l in lines if l != line]
#              if not dfs(reached_nodes + line, new_lines):
#                  # 全部つながることが確認された場合
#                  return False
#      else:
#          # 一回もひかからなかったので終了
#          print('r', reached_nodes, file=sys.stderr)
#          if len(set(reached_nodes)) < N:
#              print('True', file=sys.stderr)
#              # 無理でした。
#              return True
#          else:
#              return False
def dfs(visited_nodes, lines):
    print(visited_nodes, file=sys.stderr)
    if len(set(visited_nodes)) == N:
        print('False',file=sys.stderr)
        return False
    # 現在のノード
    for l in lines:
        if l[0] in visited_nodes or l[1] in visited_nodes:
            if not (l[0] in visited_nodes and l[1] in visited_nodes):
                return dfs(visited_nodes + l, lines)
    else:
        # 全部見たけどなかった。橋なのでTrue
        print('True', file=sys.stderr)
        return True


ans = 0
for idx in range(M):
    # idx番目の線をなくす
    lines = []
    for m in range(M):
        if m == idx:
            continue
        else:
            lines.append([A[m], B[m]])
    print('idx, lines', idx, lines, file=sys.stderr)
    # 各頂点が全頂点とつながっているか確認
    # ただたんに全頂点が入っているだけでは断絶の可能性があるので不十分
    #  if dfs(lines[0][:1], lines):
    if len(lines) == 0:
        print(1)
        exit()
    if dfs(lines[0], lines):
        ans += 1
print(ans)
