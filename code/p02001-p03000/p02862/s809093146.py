from collections import defaultdict
from collections import deque
from collections import OrderedDict
import itertools
from sys import stdin
input = stdin.readline


class PrimeComb:
  def __init__(self, MAX=666670, MOD=1000000007):
    # preprocessing: O(MAX)
    self.MAX  = MAX
    self.MOD  = MOD
    self.fac  = [0]*MAX
    self.inv  = [0]*MAX
    self.finv = [0]*MAX
    self.fac[0]  = self.fac[1] = 1
    self.finv[0] = self.finv[1] = 1
    self.inv[1]  = 1
    for i in range(2, MAX):
      self.fac[i]  = self.fac[i-1] * i % MOD
      self.inv[i]  = MOD - self.inv[MOD % i] * int(MOD / i) % MOD
      self.finv[i] = self.finv[i-1] * self.inv[i] % MOD

  def com(self, n, k):
    # compute -> nCk % self.P : O(1)
    if (n < k): return 0
    if (n < 0 or k < 0): return 0
    return self.fac[n] * (self.finv[k] * self.finv[n-k] % self.MOD) % self.MOD


def main():
  X, Y = list(map(int, input().split()))
  PC = PrimeComb()

  num_trans1 = 0
  num_trans2 = 0

  # min_ = min(X, Y) // 3
  # X -= 3*min_
  # Y -= 3*min_
  # num_trans1 += min_
  # num_trans2 += min_
  ans = 0
  for i in range(min(X, Y)//3 + 1):
    tempX = X - 3*i
    tempY = Y - 3*i
    num_trans1 = i
    num_trans2 = i

    if tempX==tempY==0:
      ans += PC.com(num_trans1+num_trans2, num_trans1)

    elif tempX > tempY:
      if tempX % 2:
        # print(0)
        continue
      if tempX//2 != tempY:
        # print(0)
        continue
      num_trans2 += tempY
      ans += PC.com(num_trans1+num_trans2, num_trans1)
    elif tempX < tempY:
      if tempY % 2:
        # print(0)
        continue
      if tempY//2 != tempX:
        # print(0)
        continue
      num_trans1 += tempX
      ans += PC.com(num_trans1+num_trans2, num_trans1)

  # print(num_trans1, num_trans2)
  print(ans % 1_000_000_007)


if(__name__ == '__main__'):
  main()
