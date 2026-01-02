from sys import stdin
#import numpy as np
 
readline = stdin.readline
 
N, Q = map(int, readline().split()) 
C = list(map(int, readline().split())) 
S = [list(map(int, readline().split())) for _ in range(Q)] 
#print(S)
def main(N, Q, C, S):    
  # Binary Indexed Tree 
  # https://juppy.hatenablog.com/entry/2018/11/17/%E8%9F%BB%E6%9C%AC_python_Binary_Indexed_Tree_%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0
  b = [0 for _ in range(N+1)]
  def BIT_query(idx): #idxまでの和(1からスタート)
    res_sum = 0
    while idx > 0:
      res_sum += b[idx]
      idx -= idx&(-idx) #一番下の位を減らす（例：13=1011 → 1010 → 1000） 
    return res_sum
  def BIT_update(idx,x): #idxをx増やした時
    while idx <= N:
      b[idx] += x
      idx += idx&(-idx) #一番下の位を繰り上げる（例：13=1011 → 1100 → 10000 ※N=16のとき） 
    return
 
  loc = [0 for _ in range(N)] #各種類の玉のうちの最右端の所在地
  S = [(S[i], i) for i in range(Q)] #クエリ
  S.sort(key = lambda s: s[0][1]) #区間の右端でソート
  #S = np.array(S, dtype = np.int64)
  #print(S)
  ans = [0 for _ in range(Q)]
  k = 0
  for j in range(N):
    if loc[C[j]-1] > 0: #玉の更新
      BIT_update(loc[C[j]-1], -1)
    loc[C[j]-1] = j+1
    BIT_update(j+1, 1)  
    
    if S[k][0][1] == j+1:
      t = BIT_query(j+1)
    while k < len(S) and S[k][0][1] == j+1: #クエリへの返答
      ans[S[k][1]] = t - BIT_query(S[k][0][0]-1)
      k += 1
    if k == len(S):
      break
  return ans
 
ans = main(N, Q, C, S)
for a in ans:
  print(a)