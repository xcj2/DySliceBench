# 最小金額を求める
# 一番高い商品に割引を適用して半額（小数点以下切り捨て）にする作業の繰り返し
# 問題詳細：https://atcoder.jp/contests/abc141/tasks/abc141_d
# 優先度付きキューを利用する
import heapq

def main():
  n, m = map(int, input().split())
  a = list(map(int, input().split()))
  pq = to_priorityqueue(a)
  pq = use_ticket(pq, m)
  print(-sum(pq))


# 優先度付きキューを作成
# heapqモジュールを利用
# pythonのheapqの場合、pop(取り出し)を行った際に最小のものから取り出される
# 今回は大きい順に取り出して利用したいため、-1を掛けてpushする（最大の値が最小になる）
def to_priorityqueue(list):
  rtn = []
  for el in list:
    heapq.heappush(rtn, -el)
  return rtn

# チケットの利用（割引の適用）
# チケットがなくなるまで、その時点で最も価格が高い商品にわりびきを適用する
# 最大まで割引を適用した結果できたキューを返す
def use_ticket(pq, t_num):
  while t_num and pq:
    el = -(heapq.heappop(pq))
    el //= 2
    heapq.heappush(pq, -el)
    t_num -= 1
  return pq

if __name__ == "__main__":
  main()