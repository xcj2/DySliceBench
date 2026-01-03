###template###
import sys
def input(): return sys.stdin.readline().rstrip()
def mi(): return map(int, input().split())
###template###

# dijkstra（経路復元できるパターン）
from collections import defaultdict
import heapq
# sからすべての頂点への最小距離を求める O(|E| log |V|)
# 戻り値は min_dist_list, routelist。
# m_d_l : [0への最小距離, 1への最小距離, 2への最小距離, ...]
#  辿り着けないノードの場合、関数内で定義した定数INFを返す
# rl : [0の直前ノード, 1の直前ノード, ...] ただしlist[始点]は-1が入る
#  （注）本来到着不可能なノードでも、INF距離で辿り着けく設定なので経路が返る
# s: startノード
# n: 頂点数
# グラフデータは辞書を使っている。{ノードID:[(to,cost)を格納したリスト],...}
#  graph[nodeID] = [(to1, cost1), (to2, cost2), ...]
# 存在しないキーがエラーになってしまうと困るので、
# graph = defaultdict(list)として、要素を空リストで初期化して生成する
def dijkstra(s: int, n: int, graph: dict) -> list:
  INF = 10 ** 10 #INF以上の経路が存在する可能性がある場合は注意か？？
  que = []    # [(最短距離, node番号)]
  routelist = [-1] * n # routelist[node番号] = 最短経路における1つ前のノード
  heapq.heappush(que, (0, s))
  min_dist_list = [INF] * n
  min_dist_list[s] = 0
  while que:
    now_dist, node = heapq.heappop(que)

    if min_dist_list[node] < now_dist:
      continue

    for to, dist in graph[node]:
      new_dist = now_dist + dist
      if min_dist_list[to] > new_dist:
        min_dist_list[to] = new_dist
        routelist[to] = node
        heapq.heappush(que, (new_dist, to))

  return min_dist_list, routelist

N, M = mi()
SGDs = [tuple(mi()) for _ in range(M)] #start, goal, distance

#dijkstra()に渡すためのグラフデータを生成する
Graph = defaultdict(list) #辞書をlist()で初期化
for s, g, d in SGDs: #start, goal, distance
  s, g = s-1, g-1 #入力が1スタートなので0スタートに訂正
  Graph[s].append((g, d)) #nodeIDがkeyになっているdict-->dict[key]（list）に(行き先番号, 距離を入れていく)
  Graph[g].append((s, d)) #無向グラフなので逆向きも入れる

#最短経路に含まれる辺をこの集合に格納していく
#格納するのはタプル(s, g)。無向グラフなので両面を入れるように注意
Contained_Edge = set()
for eachstart in range(N): #各ノードをスタート地点にする全探索
  routelist = dijkstra(eachstart, N, Graph)[1] #経路復元リストを得る
  for i, prev in enumerate(routelist):
    #prev->iというルートだと分かるので、それをContained_Edgeに入れる
    if prev+1: #prev=-1の場合は実行されない（スタート地点なので無視）
      Contained_Edge.add((i,prev))
      Contained_Edge.add((prev,i))

#全ての辺の集合
All_Edges = {(s-1,g-1) for s, g, d in SGDs}

#print(All_Edges)
#print(Contained_Edge)
#print(All_Edges - Contained_Edge)
print(len(All_Edges - Contained_Edge))

