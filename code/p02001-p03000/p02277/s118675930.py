from copy import copy

def merge(arr, left, middle, right):
    L = arr[left:middle]
    L.append([None, float('inf')])
    R = arr[middle:right]
    R.append([None, float('inf')])

    iterL, iterR = iter(L), iter(R)
    l,r = next(iterL), next(iterR)

    for index in range(left, right):
        if l[1] <= r[1]:
            arr[index] = l
            l = next(iterL)
        else:
            arr[index] = r
            r = next(iterR)


def merge_sort(arr, left, right):
    if left + 1 < right:
        pivot = (left + right) // 2
        merge_sort(arr, left,  pivot)
        merge_sort(arr, pivot, right)
        merge(arr, left, pivot, right)


def partition(arr, start, end):
    criteria = arr[end][1]
    idx1 = start
    for idx2 in range(start, end):
        if arr[idx2][1] <= criteria:
            arr[idx1],arr[idx2] = arr[idx2],arr[idx1]
            idx1 += 1
    arr[idx1],arr[end] = arr[end],arr[idx1]
    return idx1

def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot +1, end)


num = int(input())
arr = []
for index in range(num):
    sign, number = input().split()
    arr.append([sign, int(number)])

arr1 = copy(arr)
arr2 = copy(arr)

merge_sort(arr1, 0, num)
quick_sort(arr2, 0, num - 1)

print("Stable" if arr1 == arr2 else "Not stable")
for sign, number in arr2:
    print(sign + " " + str(number))
