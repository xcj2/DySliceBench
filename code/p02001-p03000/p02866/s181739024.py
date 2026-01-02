# -*- coding: utf-8 -*-

def readInts():
  return [int(s) for s in input().split(" ")]

MOD = 998244353

def solve(N, D):
  D1 = D[0]
  D = D[1:]

  if D1 != 0:
    return 0

  D.sort()

  ans = 1
  prev = 0
  prevCount = 1
  cur = 0
  while cur < len(D):
    c = 0
    while cur < len(D) and D[cur] == (prev + 1):
      cur += 1
      c += 1
    if c == 0:
      return 0

    ans *= (prevCount ** c) % MOD
    ans %= MOD
    prev += 1
    prevCount = c

  return ans

def main():
  N = readInts()[0]
  D = readInts()
  print(solve(N, D))

if __name__ == "__main__":
  main()
