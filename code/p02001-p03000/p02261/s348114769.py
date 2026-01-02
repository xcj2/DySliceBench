def bubbleSort(matrix, N):
  for i in range(N):
    for j in reversed(range(i+1, N)):
      if matrix[j][1] < matrix[j-1][1]:
        matrix[j], matrix[j-1] = matrix[j-1], matrix[j]

def selectionSort(matrix, N):
  for i in range(N):
    minj = i
    for j in range(i, N):
      if matrix[j][1] < matrix[minj][1]:
        minj = j
    if matrix[i][1] != matrix[minj][1]:
      matrix[i], matrix[minj] = matrix[minj], matrix[i]

def printList(matrix, N):
  matrix_cards = []
  for i in range(N):
    matrix_cards.append(matrix[i][0])
  print(" ".join(map(str, matrix_cards)))

n = int(input())
A = list(input().split())
B = [[] for i in range(n)]
C = [[] for i in range(n)]

for i in range(n):
  A[i] = [A[i], int(A[i][1:])]
  B[i] = A[i]
  C[i] = A[i]

bubbleSort(B, n)
selectionSort(C, n)

printList(B,n)
print("Stable")

printList(C,n)
if B == C:
  print("Stable")
else:
  print("Not stable")

