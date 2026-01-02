import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
import sys
sys.setrecursionlimit(4000)


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
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


s = ''
dp = []
def main():
    global s
    global dp
    s = input()
    t = input()

    n = len(s)
    m = len(t)

    dp = [[0 for j in range(m+1)] for i in range(n + 1)]

    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

    #  print(t)
    #  v = 0
    #  result = ''
    #  print('dp[-1]', dp[-1])
    #  for idx, i in enumerate(dp[-1]):
    #      print(idx, i)
    #      if i == v + 1:
    #          result += t[idx-1]
    #          v += 1

    #  print(result)

    #  lcs_str = ''
    #  i, j = n - 1, m - 1
    #  while i >= 0 and j >= 0:
    #      if s[i] == t[j]:
    #          lcs_str += s[i]
    #          i -= 1
    #          j -= 1
    #      elif dp[i+1][j+1] == 0:
    #          break
    #      else:
    #          if dp[i][j+1] > dp[i+1][j]:
    #              i -= 1
    #          else:
    #              j -= 1

    #  print(lcs_str[::-1])
    print_lcs(n, m)
    global ans
    print("".join(ans))

ans = []

def print_lcs(i, j):
    global s, dp, ans
    if not i or not j:
        return ''

    ret = dp[i][j]
    if ret == dp[i-1][j]:
        print_lcs(i - 1, j)
    elif ret == dp[i][j-1]:
        print_lcs(i, j-1)
    else:
        print_lcs(i - 1, j - 1)
        ans.append(s[i-1])
        #  print(s[i-1], end='', flush=True)


main()
