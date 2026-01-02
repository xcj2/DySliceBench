cardNum = lambda S:int(list(S)[1])

def bubbleSort(L, n):
  for i in range(n):
    for j in range(n-1, i, -1):
      if cardNum(L[j]) < cardNum(L[j-1]):
        L[j], L[j-1] = L[j-1], L[j]
  return L

def selectionSort(L, n):
  for i in range(n):
    minj = i
    for j in range(i, n):
      if cardNum(L[j]) < cardNum(L[minj]):
        minj = j
    L[i], L[minj] = L[minj], L[i]
  return L

def isStable(Lb, Ls):
  if Lb == Ls:
    return "Stable"
  else:
    return "Not stable"
  
N = int(input())
A = input().split()
B = [i for i in A]
LB = bubbleSort(A, N)
LS = selectionSort(B, N)
print(' '.join(map(str, LB)))
print("Stable")
print(' '.join(map(str, LS)))
print(isStable(LB, LS))
