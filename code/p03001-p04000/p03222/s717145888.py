###template###
import sys
def input(): return sys.stdin.readline().rstrip()
def mi(): return map(int, input().split())
###template###

import itertools
H, W, K = mi()

#hから、fr:左(-1), 真っ直ぐ(0), 右(1)から wに落ちてこれるような、h行の横棒の引き方は何種類あるかを返す
def howmany(fr, h, w):
  global W
  #領域外なので0を返す
  if w+fr==0 or w+fr==W+1: return 0
  #ここから先はちゃんと領域内から落ちてくる場合
  ans = 0
  #bit全探索。区間のbitにはstatus[0]~[W-2]でアクセス
  for status in itertools.product(('0','1'),repeat=W-1):
    #両端の区間を0で埋める（添字バグを回避するため
    status = ''.join(('0',''.join(status),'0')) #左から0011010みたいな感じで入ってる
    #wの左側の区間はw-1, 右側はwに対応している
    #1は横棒がある、0は横棒がない
    if '11' in status: continue
    elif fr==0:
      if status[w-1]=='1' or status[w]=='1': continue
    elif fr==1:
      if status[w]=='0': continue
    else: #fr==-1の場合
      if status[w-1]=='0': continue
    #これらをクリアした場合は条件を満たしていることになるのでans+=1
    ans += 1
  return ans % 1000000007

#DP[H行から]ストンと[W列に]落ちてくる場合の数
DP = [[0]*(W+2) for _ in range(H+1)]
DP[0][1] = 1

for h in range(1, H+1):
  for w in range(1, W+1):
  #DP[h][w]を求める。
  #まず、どこから落ちてくるか（最大3箇所）で3パターンに分ける。
    #1. まっすぐ落ちてくるパターン
    #まっすぐパターンは、「存在しない」が無いので、ifは要らない
    #DP[h-1][w]から落ちてくる
    DP[h][w] = ((DP[h-1][w-1] * howmany(-1, h, w))%1000000007 + (DP[h-1][w] * howmany(0, h, w))%1000000007 + (DP[h-1][w+1] * howmany(1, h, w))%1000000007)%1000000007

print(DP[H][K])

