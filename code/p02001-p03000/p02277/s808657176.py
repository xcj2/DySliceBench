import sys
input = sys.stdin.readline

if __name__ == '__main__':
  N = int(input())
  A=[]
  B=[]
  for _ in range(N):
    s, n = input().split()
    A.append((s, int(n)))
    B.append((s, int(n)))

  def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp
  
  def partition(A, p, r):
    x = A[r][1]
    i = p - 1
    for j in range(p, r):
      if A[j][1] <= x:
        i += 1
        swap(A, i, j)
    swap(A, i + 1, r)
    return i + 1
  
  #r含む
  def quicksort(A, p, r):
    if p < r:
      q = partition(A, p, r)
      quicksort(A, p, q - 1)
      quicksort(A, q + 1, r)

  def merge(B, left, middle, right):
    n1 = middle - left
    n2 = right - middle
    L1=[('a', 0)]*n1
    L2=[('a', 0)]*n2
    for i in range(n1):
      L1[i] = B[left + i]
    for j in range(n2):
      L2[j] = B[middle + j]
    L1.append(('z', 10**9+1))
    L2.append(('z', 10**9+1))
    #print(L1)
    #print(L2)
    i = 0
    j = 0
    for k in range(left, right):
      if L1[i][1] <= L2[j][1]:
        B[k] = L1[i]
        i += 1
      else:
        B[k] = L2[j]
        j += 1

  
  def mergeSort(B, left, right):
    if left + 1 < right:
      middle = (left + right) // 2
      mergeSort(B, left, middle)
      mergeSort(B, middle, right)
      merge(B, left, middle, right)

  
  quicksort(A, 0, N - 1)
  mergeSort(B, 0, N)
  print('Stable' if A==B else 'Not stable')
  for a in A:
    print(a[0] + ' ' + str(a[1]))

