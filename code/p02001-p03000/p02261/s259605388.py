def bubble_sort(arr):
    n = len(arr)
    flag = True
    i = 0
    while flag:
        flag = False
        for j in range(n - 1, 0, -1):
            if int(arr[j][1]) < int(arr[j - 1][1]):
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                flag = True
        i += 1
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        minj = i
        for j in range(i, n):
            if int(arr[j][1]) < int(arr[minj][1]):
                minj = j
        arr[i], arr[minj] = arr[minj], arr[i]
    return arr


def is_stable(arr, arr_sorted):
    print("Stable" if arr_sorted == sorted(arr, key=lambda x:int(x[1])) else "Not stable")


n = int(input())
arr = input().split()
arr_b = bubble_sort(arr[:])
arr_s = selection_sort(arr[:])

print(*arr_b)
is_stable(arr, arr_b)
print(*arr_s)
is_stable(arr, arr_s)

