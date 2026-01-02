def partition(A,p,r):
  q = p
  for i in range(p,r):
    if A[i][1] <= A[r][1]:
      A[q],A[i] = A[i],A[q]
      q += 1

  A[q],A[r] = A[r],A[q]
  return q

def quicksort(A,left,right):
  if left < right:
    q = partition(A,left,right)
    quicksort(A,left,q-1)
    quicksort(A,q+1,right)

def check_stable(A):
  for i in range(1,len(A)):
    if A[i-1][1] == A[i][1]:
      if A[i-1][2] > A[i][2]:
        return "Not stable"
  return "Stable"

n = int(input())
data = []
for i in range(n):
  mark, num = map(str,input().split())
  data += [[mark,int(num),i]]

quicksort(data,0,len(data) -1)
print(check_stable(data))

for line in data:
  print(line[0],line[1])

