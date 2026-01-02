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

A, B, Q = LI()
s_list = []
t_list = []
for i in range(A):
  s_list.append(II())
for j in range(B):
  t_list.append(II())
x_list = []
for q in range(Q):
  x_list.append(II())
  
import bisect
for x in x_list:
  # x の左右で最も近い神社と寺をそれぞれ探しておく
  # bisectが0の場合は左はなく、len(x)の場合は
  tidx = bisect.bisect_left(t_list, x)
  if tidx == 0:
    tl = 9*10**11
  else:
    tl = t_list[tidx-1]
  if tidx == len(t_list):
    tr = 9*10**11
  else:
    tr = t_list[tidx]

  sidx = bisect.bisect_left(s_list, x)
  if sidx == 0:
    sl = 9*10**11
  else:
    sl = s_list[sidx-1]
  if sidx == len(s_list):
    sr = 9*10**11
  else:
    sr = s_list[sidx]

  dsl = abs(x-sl)
  dsr = abs(x-sr)
  dtl = abs(x-tl)
  dtr = abs(x-tr)

  print(min(max(dsl, dtl), max(dsr, dtr), dsl+dtr+min(dsl, dtr), dsr+dtl+min(dsr,dtl)))
  