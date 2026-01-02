###template###
import sys
def input(): return sys.stdin.readline().rstrip()
def mi(): return map(int, input().split())
###template###
import sys
sys.setrecursionlimit(10000000)

N = int(input())

adj = [set() for _ in range(N)] #adj[i] = (i_adj, 距離0or1)
for _ in range(N-1):
  u, v, w = mi()
  #0スタートに
  u -= 1
  v -= 1
  adj[u].add((v, w%2))
  adj[v].add((u, w%2))

from collections import deque
q = deque([])

seen = [0] * N
bw = [0] * N

#とりあえずノード0から探索をスタートすることにする
#0の距離は0としておく
q.append(0)
bw[0] = 0 #必要無いが、分かりやすくするために
seen[0] = 1


def solve(): #前のノードまでの色（0or1）を引き継ぐ
  try: nownode = q.popleft()
  except: return
  nowcolor = bw[nownode]

  #今のノードから隣接しているものを探索
  for adjidx, w in adj[nownode]:
    if seen[adjidx]!=1:
      q.append(adjidx)
      seen[adjidx]=1
      bw[adjidx] = (nowcolor+w)%2

  solve()

solve()

for color in bw:
  print(color)

