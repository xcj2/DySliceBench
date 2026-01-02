import math
n = int(input())
A = []

def partition(A,p,r):

    x = A[r-1][1]
    i = p-1

    for j in range(p,r-1):
        if A[j][1] <= x:
            i += 1
            tmp = A[j]
            A[j] = A[i]
            A[i] = tmp
    tmp = A[i+1]
    A[i+1] = A[r-1]
    A[r-1] = tmp

    return i+1


def QuickSort(A,p,r):
    if p<r:
        q = partition(A,p,r)
        QuickSort(A,p,q)
        QuickSort(A,q+1,r)


def merge(A, left, mid, right):

  L = A[left:mid]
  L.append((1,math.inf))
  R = A[mid:right]
  R.append((1,math.inf))
  i = 0
  j = 0
  for k in range(left,right):

    if L[i][1] <= R[j][1]:
      A[k] = L[i]
      i = i + 1
    else:
      A[k] = R[j]
      j = j + 1


def mergeSort(A,left,right):
    if left +1 < right:
        mid = (left+right) // 2
        mergeSort(A,left,mid)
        mergeSort(A,mid,right)
        merge(A,left,mid,right)



for i in range(n):
   color,number =input().split()
   A.append((color,int(number)))

A_merge = A.copy()
A_quick = A.copy()

mergeSort(A_merge,0,n)
QuickSort(A_quick,0,n)


if A_quick==A_merge: print("Stable")
else: print("Not stable")

for x in A_quick:
    print("%s %d" %(x[0],x[1]))
