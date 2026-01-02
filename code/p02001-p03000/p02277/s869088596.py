def merge(A, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L, R = A[left: left + n1], A[mid: mid + n2]

    L.append([0,2000000000])
    R.append([0,2000000000])

    i, j = 0, 0
    for k in range(left, right):
        #print("k", k, "l", left, "m", mid, "r", right, "L", L, "R", R)
        if L[i][1] <= R[j][1]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def mergeSort(A, left, right):
    #print("l", left, "r", right)
    if left + 1 < right:
        mid = (left + right) // 2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)


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


n = int(input())
cards = []
merge_cards = []
for _ in range(n):
    tmp = input().split(' ')
    cards.append([tmp[0], int(tmp[1])])
    merge_cards.append([tmp[0], int(tmp[1])])

mergeSort(merge_cards, 0, n)

quick_sort(cards, 0, n - 1)

if merge_cards == cards:
    print("Stable")
else:
    print("Not stable")

for card in cards:
    print(*card)
