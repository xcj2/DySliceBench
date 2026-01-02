class Card:
    def __init__(self,m, v):
        self.m = m
        self.v = v
    
    def __repr__(self):
        return str(self.m) + ' ' + str(self.v)


def quicksort(A, p, r):
    #print("init",p,r)
    if p < r:
        #print("calcq")
        q = partition(A, p, r)
        #print("q=",q)
        #print("sortleft")
        quicksort(A, p,q-1)
        #print("sortright")
        quicksort(A,q+1,r)

def partition(A, p, r):
  x = A[r]
  i = p-1
  #print("s",A,p,r,i)
  for j in range(p,r):
    #print("compr",A[j],x)
    if A[j].v <= x.v:
      i = i+1
      #print("change! idx", i ,j)
      A[i], A[j] = A[j], A[i]
    #print(A)
  A[i+1],A[r] = A[r], A[i+1]
  #print("e",A,p,r,i+1)
  return i+1

cnt = 0
def merge(A, left, mid, right):
  global cnt
  n1 = mid - left
  n2 = right - mid
  #L = [0] * (n1+1)
  #R = [0] * (n2+1)
  #print("init ",left,mid,right,A[left:mid],A[mid:right],n1,n2)
  L = [Card(None,None) for i in range(n1+2)]
  R = [Card(None,None) for i in range(n2+2)]
  #print("check ", L, R)
  for i in range(n1):
    L[i] = A[left + i]
  for i in range(n2):
    R[i] = A[mid + i]
  L[n1].v = 9999999999999
  R[n2].v = 9999999999999
  #print("split ",n1,n2, L, R)
  i = 0
  j = 0
  for k in range(left,right):
    cnt+=1
    if L[i].v <= R[j].v:
      A[k] = L[i]
      i = i + 1
    else:
      A[k] = R[j]
      j = j + 1
  #print("reslt ",A)

def mergeSort(A, left, right):
  #print("margeSort ",A[left:right])
  if left+1 < right:
    mid = int((left + right)/2)
    mergeSort(A, left, mid)
    mergeSort(A, mid, right)
    merge(A, left, mid, right)

A1 = []
A2 = []
n = int(input())

for i in range(n):
    A = input().split()
    A1.append(Card(A[0],int(A[1])))
    A2.append(Card(A[0],int(A[1])))

quicksort(A1,0,n-1)

mergeSort(A2,0,n)

flag = True
for i in range(n):
    if A1[i].m != A2[i].m:
        flag = False
        print("Not stable")
        break    
if flag:
    print("Stable")

for i in range(0,n):
    print(A1[i])
    #print(A2[i])

