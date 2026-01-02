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

N = _I()
A = LI()

#  # 山1の雨量は、左右のダムの大きい方
#  # 山1の雨量は、左右の山を見て候補値を絞り込む
#  # 例えば左右にそれぞれ6と4溜まっている場合、自分を0,2,4降った可能性を検討する
#  # ダムxの水量を見て、ありうる候補を見つける
#  # 最小値から見ると速いかも
#  # 山を-2すると、ダムを-2することができる
#  # 最小のダムを見つける
#  min_dam = min(A)
#  min_dam_idx = A.index(min_dam)
#  tmp_A = A[min_dam_idx:] + A[:min_dam_idx]
#  if min_dam == 0:
#      # 0のダムがある場合、その周りのダムは0が確定する
#      yamas = [0,0]
#      for i in range(2, N):
#          yamas.append(int((tmp_A[i]-yamas[-1]/2)*2))
#      yamas = yamas[N-min_dam_idx:] + yamas[:N-min_dam_idx]
#      print(yamas)
#  else:
#      # 最小のダムが0になるまで-2していく
#      tmp_A = [i - min_dam for i in tmp_A]
#      print(tmp_A)
#      yamas = [0,0]
#      for i in range(2, N):
#          yamas.append(int((tmp_A[i]-yamas[-1]/2)*2))
#      yamas = yamas[N-min_dam_idx:] + yamas[:N-min_dam_idx]
#      print(yamas)


'''
コンテスト後
雨の総量をSとおくと、
S = A1 + A2 + ... An
S = (W1+ W2 + ... Wn)/2
A1 = (W1+W2)/2
つまり、
2 = (W1+W2)/2
A2 = (W2+W3)/2
つまり、
2 = (W2 + W3)/2
S = 2A1 + 2A3 + ... 2AN//2

W1 = S - (W2 + W3 + ... Wn) = S - 2(A2 + A4 ... + An-1)
W1 = 8 - 2(2)
W2 = 8 - 2()

W1 + W2 = 2A1
W2 = 2A1 - W1
W2 = 2*2 - 4 = 0
W3 = 2A2 - W2 = 2*2 - 0 = 4
'''

S = sum(A)
W = [0 for i in range(N)]
W[0] = S - 2*sum([i for idx, i in enumerate(A[1:]) if idx % 2 == 0])
for i in range(1, N):
    W[i] = 2*A[i-1] - W[i-1]
for w in W:
    print(w, end=' ')
