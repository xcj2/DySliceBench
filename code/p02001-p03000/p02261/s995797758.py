def bubbleSort(A):
  global N
  for i in range(N):
    for j in  range(N-1,i,-1):
      jn = int(A[j][1:])
      jm =  int(A[j-1][1:])
      if jn < jm:
        x = A[j]
        A[j] = A[j-1]
        A[j-1] = x

def selectionSort(A):
  global N
  for i in range(N):
    minj = i
    for j in range(i,N):
      jn = int(A[j][1:])
      jm =  int(A[minj][1:])
      if jn < jm:
        minj = j
    if minj != i :
      x = A[minj]
      A[minj] = A[i]
      A[i] = x

def stableDict(A):
  S = dict()
  for e in A:
    i = e[1:]
    if i in S:
      S[i] = e + S[i]
    else:
      S[i] = e
  return S

def ckStable(org,dst):
  dictOrg = stableDict(org)
  dictDst = stableDict(dst)
  stableFlg = True
  for a in dictOrg.keys():
    if dictOrg[a] != dictDst[a]:
      stableFlg = False
  if stableFlg :
    print("Stable")
  else:
    print("Not stable")

N = int(input())
A = list(input().split())

A1 = list(A)
A2 = list(A)

bubbleSort(A1)
print(" ".join(A1))
ckStable(A,A1)
  
selectionSort(A2)
print(" ".join(A2))
ckStable(A,A2)
