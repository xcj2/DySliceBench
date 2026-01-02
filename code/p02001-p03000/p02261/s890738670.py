def bubble_sort(c, n):
  l = c[:]
  for i in range(n-1):
    for j in reversed(range(i+1, N)):
      if l[j][1] < l[j-1][1]:
        l[j], l[j-1] = l[j-1], l[j]
  return l

def selection_sort(c, n):
  l = c[:]
  for i in range(n):
    min_x = i
    for j in range(i, n):
      if l[j][1] < l[min_x][1]:
        min_x = j
    l[i], l[min_x] = l[min_x], l[i]
  return l

def is_stable(in_arr, out_arr, n):
  for i in range(n):
    for j in range(i+1, n):
      for a in range(n):
        for b in range(a+1, n):
          if in_arr[i][1] == in_arr[j][1] and in_arr[i] == out_arr[b] and in_arr[j] == out_arr[a]:
            return False
  return True


N = int(input())
C = list(map(list, input().split()))

bubble_sorted_list = bubble_sort(C, N)
selection_sorted_list = selection_sort(C, N)

print(" ".join(map("".join, bubble_sorted_list)))
print("Stable" if is_stable(C, bubble_sorted_list, N) else "Not stable")
print(" ".join(map("".join, selection_sorted_list)))
print("Stable" if is_stable(C, selection_sorted_list, N) else "Not stable")

