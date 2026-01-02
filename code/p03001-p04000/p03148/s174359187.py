import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7

def score(td):
  t_list = [v[0] for v in td]
  d_list = [v[1] for v in td]
  ut = len(set(t_list))
  score_ut = ut**2
  score_d = sum(d_list)
  return score_ut + score_d
  
def solve():
  N, K = LI()
  td = []
  for i in range(N):
    t, d = LI()
    td.append([t, d])

  from operator import itemgetter
  td.sort(key=itemgetter(1), reverse=True)

  # おいしさtopK
  cand = td[:K]
  
  # cand のネタ保持数dict
  import collections
  c = collections.Counter([v[0] for v in cand])
  m = len(c.keys())
  
  # 持ってないネタのtop1リスト
  rest_top1 = {}
  for v in td:
    if v[0] not in c:
      if v[0] not in rest_top1:
      	rest_top1[v[0]] = v[1]
      else:
        if rest_top1[v[0]] < v[1]:
          rest_top1[v[0]] = v[1]
          
  # スコア降順
  rest_o = sorted([v for k, v in rest_top1.items()], reverse=True)
  current_score = score(cand)
  scores = [current_score]
  if len(rest_o) == 0:
    print(current_score)
    return
  # おいしく無い順に持ってないもののtop1と入れ替え
  nget = 0
  for i in range(1, K):
    target = cand[-i]
    if c[target[0]] == 1:
      continue # 一つしか持ってないなら入れ替えない
    
    # スコアの差分を作る
    # netaボーナス
    dscore_neta = (m+nget+1)**2 - (m+nget)**2 
    # おいしさボーナス
    dscore_d = -target[1] + rest_o[nget]
    current_score += dscore_neta
    current_score += dscore_d
    
    scores.append(current_score)
    # 状態更新
    nget += 1
    c[target[0]] -= 1
    
    # 全部取ったらおわり
    if nget == len(rest_o):
      break
  print(max(scores))
solve()