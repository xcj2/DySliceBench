#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: Jul, 13, 2020 05:11:35 by Nobody
# $Author$
# $Date$
# $URL$
__giturl__ = "$URL$"


from sys import stdin
input = stdin.readline


class PrimeComb:
  def __init__(self, MAX=510000, MOD=1000000007):
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
  N, K = list(map(int, input().split()))

  MOD = 1_000_000_007
  PC = PrimeComb()
  for i in range(1, K+1):
    print(PC.com(N-K+1, i) * PC.com(K-1, i-1) % MOD)


if(__name__ == '__main__'):
  main()
