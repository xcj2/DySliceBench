import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools, os, queue
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
def perr(s): return print(s, file=sys.stderr)
def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('- {} -> {}'.format(name, val), file=sys.stderr)
            return None
N, M =LI()
AB = []
for i in range(N):
    AB.append(LI())
#  AB.sort(key=lambda x: x[0])
#  perr(AB)
AB_dict = {}
for ab in AB:
    if ab[0] not in AB_dict.keys():
        AB_dict[ab[0]] = [ab[1]]
    else:
        AB_dict[ab[0]].append(ab[1])
#  for k in AB_dict.keys():
#      AB_dict[k] = collections.Counter(AB_dict[k])
#  for k in AB_dict.keys():
#      AB_dict[k].sort()
perr(AB_dict)

#  tmp = []
#  day = 1
#  ans = 0
#  crr = 0
#  while True:
#      if day == M + 1:
#          break

#      if crr < N:
#          if AB[crr][0] > day:
#              perr('nextday')
#              perr(tmp)
#              day += 1
#              if len(tmp) == 0:
#                  continue
#              tmp.sort()
#              ans += tmp.pop()
#          else:
#              perr('add')
#              tmp.append(AB[crr][1])
#              crr += 1
#      else:
#          if len(tmp) == 0:
#              break
#          tmp.sort()
#          for time in range(M-day+1):
#              ans += tmp.pop()
#              day += 1
        
#  print(ans)
#  ans = 0
#  tmp = []
#  crr = 0
#  for i in range(1, M+1):
#      if crr < N:
#          if AB[crr][0] == i:
#              while True:
#                  if crr == N:
#                      break
#                  if AB[crr][0] != i:
#                      break
#                  tmp.append(AB[crr][1])
#                  crr += 1

#      perr('tmp')
#      perr(tmp)
#      if len(tmp) == 0:
#          continue

#      max_v = max(tmp)
#      ans += max_v
#      tmp.remove(max_v)
#      #  tmp.sort()
#      #  ans+=tmp.pop()

#  """
#  貪欲か？
#  日が長くて報酬の高いものから選んでいく
#  そうすると
#  10 1
#  9 10
#  みたいなときに10 1のほうから選んでしまうからだめ
#  残り日数を意識
#  残ってる中で最も報酬の高いものから？
#  2 10
#  1 11
#  のパターンで、先に1をやってしまうためだめ
#  2 10
#  1 11
#  1 15
#  のパターンで、1 1をやるのが正解
#  """

ans = 0
tmp = queue.PriorityQueue()
keys = AB_dict.keys()
for i in range(1, M+1):
    # 残りi日
    if i in keys:
        for ab in AB_dict[i]:
            tmp.put((-ab, ab))
        #  tmp[len(tmp):] = AB_dict[i]
    perr('tmp')
    perr(tmp)
    if tmp.empty():
        continue
    #  tmp.sort()
    #  max_v = max(tmp)
    #  ans += max_v
    ans += tmp.get()[1]
print(ans)
