# -*- coding: utf-8 -*-

def readInts():
  return [int(s) for s in input().split(" ")]

def readChars(S, c, i):
  count = 0
  for k in range(i, len(S)):
    if S[k] == c:
      count += 1
    else:
      return (k, count)
  return (len(S), count)

def solve():
  S = input()
  ans = [0 for _ in range(len(S))]
  i = 0
  while i < len(S):
    j, countR = readChars(S, 'R', i)
    i, countL = readChars(S, 'L', j)
    ans[j-1] += (countR // 2) + (countR % 2) + (countL // 2)
    ans[j] += (countR // 2) + (countL // 2) + (countL % 2)
  print(" ".join(map(str, ans)))

def main():
  solve()

if __name__ == "__main__":
  main()
