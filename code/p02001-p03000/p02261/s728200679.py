import copy

n = int(input())
arr1 = [(int(x[-1]), x) for x in list(input().split())]
arr2 = copy.copy(arr1)

def bubble_sort(arr, n):
  for i in range(n):
    for j in reversed(range(i + 1, n)):
      if arr[j][0] < arr[j-1][0]:
        arr[j], arr[j-1] = arr[j-1], arr[j]

def select_sort(arr, n):
  for i in range(n):
    minj = i
    for j in range(i, n):
      if arr[j][0] < arr[minj][0]:
        minj = j
    arr[i],arr[minj] = arr[minj],arr[i]

def check_stable(input, output):
  return 'Stable' if input == output else 'Not stable'

def arr_to_map(input):
  return ' '.join([x[1] for x in input])

bubble_sort(arr1, n)
select_sort(arr2, n)

print (arr_to_map(arr1))
print ('Stable')
print (arr_to_map(arr2))
print (check_stable(arr1, arr2))
