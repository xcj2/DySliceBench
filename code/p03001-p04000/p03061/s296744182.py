# -*- coding: utf-8 -*-

def readInts():
  return [int(s) for s in input().split(" ")]

def gcd(m, n):
  m, n = max(m, n), min(m, n)
  if n == 0:
    return m
  return gcd(n, m % n)

def gcds(A):
  ret = A[0]
  for n in A[1:]:
    ret = gcd(ret, n)
  return ret

def main():
  N = readInts()[0]
  A = readInts()

  lgcds = [1 for _ in range(N)]
  lgcds[0] = A[0]
  for i in range(N-1):
    lgcds[i+1] = gcd(lgcds[i], A[i+1])

  rgcds = [1 for _ in range(N)]
  rgcds[N-1] = A[N-1]
  for i in range(1, N):
    rgcds[N-1-i] = gcd(rgcds[N-i], A[N-1-i])

  m = 1
  for i in range(N):
    if i == 0:
      m = max(m, rgcds[i+1])
    elif i == N - 1:
      m = max(m, lgcds[i-1])
    else:
      m = max(m, gcd(lgcds[i-1], rgcds[i+1]))
  print(m)

if __name__ == "__main__":
  main()
