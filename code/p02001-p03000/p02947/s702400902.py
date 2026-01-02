import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools, os
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
def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('- {} -> {}'.format(name, val), file=sys.stderr)
            return None

N = _I()
S = []
for i in range(N):
    S.append(input())

"""
a-zの文字数カウントする
[1,1,0,,,]
[1,1,0,,,]
[1,2,1,,,]

などのリストが得られる。
setしてカウント
"""

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
#  ex = [chr(ord('a') + i) for i in range(26)]
#  s_counts = []
#  for s in S:
#      s_count = []
#      for a in ex:
#          s_count.append(s.count(a))
#      s_counts.append(s_count)

#  #  print(s_counts)

#  ans = 0
#  done_list = []
#  for s_count in s_counts:
#      if s_count in done_list:
#          continue
#      else:
#          done_list.append(s_count)
#          cnt = s_counts.count(s_count)
#          if cnt == 1:
#              continue
#          else:
#              ans += combinations_count(cnt, 2)
chars = []
for s in S:
    char_list = []
    for char in s:
        char_list.append(char)
    char_list.sort()
    char_list = ''.join(char_list)
    chars.append(char_list)
#  print(chars)
ans = 0
done_list = []
char_counts = {}
for char in chars:
    if char in char_counts.keys():
        char_counts[char] += 1
    else:
        char_counts[char] = 1
for char_count in char_counts.values():
    if char_count == 1: continue


    ans += combinations_count(char_count, 2)
print(ans)
