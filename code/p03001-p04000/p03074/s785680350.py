# -*- coding: utf-8 -*-

def readInts():
  return [int(s) for s in input().split(" ")]

def solve(N, K, S):
  chunks = []
  current = '1'
  count = 0
  for i, c in enumerate(S):
    if c != current:
      chunks.append(count)
      current = '0' if current == '1' else '1'
      count = 0
    count += 1
  chunks.append(count)
  if current == '0':
    chunks.append(0)

  if len(chunks) < 2 * K + 1:
    return N

  cSums = [0 for _ in range(len(chunks) + 1)]
  for i, c in enumerate(chunks):
    cSums[i + 1] = cSums[i] + c

  ans = 0
  for i in range(0, len(cSums) - (2 * K + 1), 2):
    ans = max(ans, cSums[i + 2 * K + 1] - cSums[i])

  return ans

def main():
  N, K = readInts()
  S = input()

  print(solve(N, K, S))

if __name__ == "__main__":
  main()
