# import math
# import itertools
# import numpy as np

def insertionSort(A, n, g, cnt):
  for i in range(g,n):
    v = A[i]
    j = i - g
    
    while j >= 0 and A[j] > v:
      A[j+g] = A[j]
      j = j - g   
      cnt += 1

    A[j+g] = v

  return [A, cnt]

def shellSort(A, n):
  cnt = 0

  # if n > 4:
  #   G = [4,1]
  # else:
  #   G = [1]

  G = [1]
  i = 1

  while G[0] + 3 ** i < n:
    G.insert(0, G[0] + 3 ** i)
    i += 1

  m = len(G)

  for i in range(m):
    A, cnt = insertionSort(A, n, G[i], cnt)

  return [m, G, A, cnt]

def main():
  n = int(input())
  A = [int(input()) for _ in range(n)]

  m, G, A, cnt = shellSort(A, n)

  print(m)
  print(*G)
  print(cnt)
  for num in A:
    print(num)

if __name__ == '__main__':
  main()
