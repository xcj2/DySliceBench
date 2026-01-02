# -*- coding: utf-8 -*-

def readInts():
  return [int(s) for s in input().split(" ")]

def max_val(V, n):
  count = n
  ret = 0
  for v in sorted(V):
    if v < 0 and count > 0:
      count -= 1
    else:
      ret += v
  return ret

def main():
  N, K = readInts()
  V = readInts()

  ans = 0

  for KL in range(K+1):
    KR = K - KL
    for L in range(min(KL, N)+1):
      for R in range(min(KR, N-L)+1):
        left = V[:L]
        right = V[-1 * R:] if R > 0 else []
        s = max_val(left, KL - L) + max_val(right, KR - R)
        ans = max(ans, s)

  print(ans)

if __name__ == "__main__":
  main()
