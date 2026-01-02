def partition(A, p, r):
 x = A[r]
 i  = p-1
 for j in range(p,r):
  if int(A[j][1]) <= int(x[1]):
   i += 1
   A[i],A[j] = A[j],A[i]
 A[i+1],A[r] = A[r],A[i+1]
 return i+1

def quicksort(A, p, r):
 if p < r:
  q = partition(A, p, r)
  quicksort(A, p, q-1)
  quicksort(A, q+1, r)

def merge(A, left, mid, right):
    L = A[left:mid] + [[0,1000000001]]
    R = A[mid:right] + [[0,1000000001]]
    i = j = 0
    for k in range(left, right):
        if int(L[i][1]) <= int(R[j][1]):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
 
def mergeSort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)


n = int(input())
A = [input().split() for i in range(n)]
B = A[:]
quicksort(A, 0, n-1)
mergeSort(B, 0, n)

juge = 1
for i in range(n):
 if A[i] != B[i]:
  juge = 0
  break
if juge == 1:
 print("Stable")
else:
 print("Not stable")

for i in range(n):
 print(" ".join(A[i]))