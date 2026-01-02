import copy

n = int(input())

Card1 = []

for i in range(n):
  Card1.append(input())

def partition(B, p, r):
  x1, x2 = B[r].split()
  global i
  i = p-1
  for j in range(p, r):
    c1, c2 = B[j].split()
    if int(c2) <= int(x2):
      i += 1
      y = B[i]
      z = B[j]
      B[i] = z
      B[j] = y
  a = B[i+1]
  b = B[r]
  B[i+1] = b
  B[r] = a
  return i+1

def quicksort(B, p, r):
  if p < r:
    q = partition(B, p, r)
    quicksort(B, p, q-1)
    quicksort(B, q+1, r)

def merge(A, left, mid, right):
  inf = float('inf')
  L = A[left:mid] + ["D inf"]
  R = A[mid:right] + ["D inf"]
  i = 0
  j = 0
  for k in range(left, right):
    l1 = L[i].split()
    r1 = R[j].split()
    l2 = float(l1[1])
    r2 = float(r1[1])
    if l2 <= r2:
      A[k] = L[i]
      i += 1
    else:
      A[k] = R[j]
      j += 1

def mergesort(A, left, right):
  if left+1 < right:
    mid = (left + right)//2
    mergesort(A, left, mid)
    mergesort(A, mid, right)    
    merge(A, left, mid, right)

Card2 = copy.deepcopy(Card1)

quicksort(Card1, 0, n-1)

mergesort(Card2, 0, n)

if Card1 == Card2:
  print("Stable")
else:
  print("Not stable")

for i in range(n):
  print(Card1[i])
