T = int(input())

def hakidasi(L):
  n = len(bin(max(L))) - 2
  k, end = 0, len(L)
  for i in range(n - 1, -1, -1):
    for j in range(k, end):
      if (L[j] >> i) & 1:
        L[k], L[j] = L[j], L[k]
        break
    else:
      continue
    k += 1
    for j in range(end):
      if j == k - 1: continue
      if (L[j] >> i) & 1:
        L[j] ^= L[k - 1]
  return L

def judge(L, x):
  if L == []:
    return False
  n = len(bin(max(L))) - 2
  m = len(L)
  for i in range(m):
    a = len(bin(x))
    b = len(bin(L[i]))
    if a == b:
      x ^= L[i]
    elif a > b:
      return False
    if x == 0:
      return True
  return False

def main():
  N = int(input())
  A = list(map(int, input().split()))
  S = input()
  U = 60
  
  L = []
  for i in range(N - 1, -1, -1):
    if A[i] == 0:
      continue
    n = int(S[i])
    if n == 0:
      L.append(A[i])
      L = hakidasi(L)
      if L[-1] == 0:
        L.pop()
    else:
      m = judge(L, A[i])
      if m == False:
        return 1
  return 0

for i in range(T):
  print(main())
