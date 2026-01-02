
class Card():
  def __init__(self, suit, value):
    self.suit = suit
    self.value = int(value)
  
  def __str__(self):
    return " ".join([self.suit, str(self.value)])
  


MAXINT = 1000000000 + 1
def mergesort(X, l, r):
  if l + 1 < r:
    m = (l + r)//2
    mergesort(X,l,m)
    mergesort(X,m ,r)
    merge(X,l, m, r)

def merge(X, l, m, r):
  nl = m - l
  nr = r - m
  L = [X[i] for i in range(l, l + nl)]
  R = [X[i] for i in range(m, m + nr)]
  L.append(Card('', MAXINT))
  R.append(Card('', MAXINT))
  i = 0
  j = 0
  for k in range(l,r):
    if L[i].value <= R[j].value:
      X[k] = L[i]
      i += 1
    else:
      X[k] = R[j]
      j += 1

def swap(A, i, j):
  tmp = A[i]
  A[i] = A[j]
  A[j] = tmp

def partition(S, p, r):
  x = S[r]
  i = p -1
  for j in range(p,r):
    if S[j].value <= x.value:
      i += 1
      swap(S, i, j)
  swap(S, i+1, r)
  return i+1

def quicksort(S, p, r):
  if p < r:
    q = partition(S, p, r)
    quicksort(S, p, q-1)
    quicksort(S, q+1, r)

n = int(input())
A = list()
B = list()
for _ in range(n):
  s, v = input().split()
  A.append(Card(s, v))
  B.append(Card(s, v))

mergesort(A, 0, len(A))
quicksort(B, 0, len(B) - 1)

flag = True
for a,b in zip(A,B):
  if a.suit != b.suit:
    flag = False
    break

if flag:
  print("Stable")
else:
  print("Not stable")

for x in B:
  print(x)

