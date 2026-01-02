N = int(input())
A = input().split(" ")

def bubble_sort(A):
  N = len(A)
  for i in range(N):
    for j in range(N - 1, i, -1):
      if int(A[j][1]) < int(A[j - 1][1]):
        A[j - 1], A[j] = A[j], A[j - 1]
  return A

def selection_sort(A):
  N = len(A)
  for i in range(N):
    mini = i
    for j in range(i + 1, N):
      if int(A[j][1]) < int(A[mini][1]):
        mini = j
    if mini != i:
      A[mini], A[i] = A[i], A[mini]
  return A

def is_stable(A, B):
  map_a = {}
  map_b = {}
  for i in range(len(A)):
    s_a = A[i][0]
    s_b = B[i][0]
    v_a = A[i][1]
    v_b = B[i][1]
    if v_a in map_a:
      map_a[v_a].append(s_a)
    else:
      map_a[v_a] = [s_a]
    if v_b in map_b:
      map_b[v_b].append(s_b)
    else:
      map_b[v_b] = [s_b]

  result = True
  for k in map_a:
    if len(map_a[k]) > 1:
      result = result and (map_a[k] == map_b[k])

  return result

A_sorted = bubble_sort(A[:])
print(" ".join(A_sorted))
print("Stable") if is_stable(A, A_sorted) else print("Not stable")

A_sorted = selection_sort(A[:])
print(" ".join(A_sorted))
print("Stable") if is_stable(A, A_sorted) else print("Not stable")