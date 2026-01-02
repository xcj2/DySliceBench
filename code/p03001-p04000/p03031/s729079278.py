# -*- coding: utf-8 -*-

def readInts():
  return [int(s) for s in input().split(" ")]

def is_on(L, i):
  if L & (1 << (i-1)):
    return True
  else:
    return False

def is_ok(L, s, p):
  c = 0
  for i in s:
    if is_on(L, i):
      c += 1
  return (c % 2) == p

def main():
  N, M = readInts()
  S = []
  for _ in range(M):
    data = readInts()
    S.append(data[1:])
  P = readInts()

  ans = 0
  for L in range(2**N):
    ok = True
    for i, s in enumerate(S):
      if not is_ok(L, s, P[i]):
        ok = False
        break
    if ok:
      ans += 1

  print(ans)

if __name__ == "__main__":
  main()
