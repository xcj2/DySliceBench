import math
from collections import deque

def create_table(N, A):
    num_block = int(-(-math.log2(N)//1)) + 1
    dp = [[-1]*num_block for i in range(N)]
    for i in range(N):
        dp[i][0] = i
    for k in range(1, num_block):
        for i in range(N):
            e = min(N-1, i + (1 << (k - 1)))
            former = dp[i][k-1]
            later = dp[e][k-1]
            if A[former] > A[later]:
                dp[i][k] = later
            else:
                dp[i][k] = former
            if e == N-1:
                break
    return dp

def query(i, j, dp, A):
    if i == j:
      return i
    length = int(math.log2(abs(i-j)))
    former = dp[i][length]
    later = dp[j-(1<<length)+1][length]
    if A[former] > A[later]:
        return later
    return former
      
def run():
  N = int(input())
  g = {}
  for n in range(N):
    kc = list(map(int, input().split()))
    g[n] = kc[1:]
  Q = int(input())
  uv = [tuple(map(int, input().split())) for q in range(Q)]
  euler = []
  depths = []
  order = [-1]*N
  def dfs(now, pred, d):
    stacks = deque([(now, pred, d)])
    while stacks:
      now, pred, d = stacks.pop()
      euler.append(now)
      depths.append(d)
      if order[now] != -1:
        continue
      if order[now] == -1:
        order[now] = len(euler) - 1
      for nxt in g[now]:
        if nxt == pred:
          continue
        stacks.append((now, pred, d))
        stacks.append((nxt, now, d+1))
  dfs(0, -1, 0)
  #RMQ
  len_li = len(depths)
  dp = create_table(len_li, depths)
  #LCA
  for u, v in uv:
    o1, o2 = order[u], order[v]
    o1, o2 = min([o1, o2]), max([o1, o2])
    o = query(o1, o2, dp, depths)
    print(euler[o])
    if len(uv) == 1:
      exit()
  
if __name__ == '__main__':
  run()
