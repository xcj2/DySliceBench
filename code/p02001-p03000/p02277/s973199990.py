def partition(A, p, r):
  x = A[r][1]
  i = p - 1
  for j in range(p, r):
    if A[j][1] <= x:
      i += 1
      A[i], A[j] = A[j], A[i]
  A[i + 1], A[r] = A[r], A[i + 1]
  return i + 1

def quick_sort(A, p, r):
  if p < r:
    q = partition(A, p, r)
    quick_sort(A, p, q - 1)
    quick_sort(A, q + 1, r)

def is_stable(A, B):
  ma = {}
  for suit, num in A:
    if num not in ma: ma[num] = []
    ma[num].append(suit)

  mb = {}
  for suit, num in B:
    if num not in mb: mb[num] = []
    mb[num].append(suit)

  for num in ma:
    if ma[num] != mb[num]: return False

  return True

N = int(input())
A = []
for i in range(N):
  suit, num = input().split()
  A.append([suit, int(num)])

B = A[:]
quick_sort(A, 0, len(A) - 1)
print("Stable" if is_stable(A, B) else "Not stable")
for suit, num in A: print("{} {}".format(suit, num))