from copy import deepcopy

def BubbleSort(a, N):
    for i in range(N):
        for j in range(N-1, i, -1):
            if a[j][1] < a[j-1][1]:
                a[j], a[j-1] = a[j-1], a[j]
    return a

def SelectionSort(a, N):
    for i in range(N):
        minj = i
        for j in range(i+1, N):
            if a[minj][1] > a[j][1]:
                minj = j
        a[minj], a[i] = a[i], a[minj]
    return a

def isStable(x, bubble):
    if x == bubble: return "Stable"
    else: return "Not stable"

if __name__ ==  "__main__":
    N = int(input())
    a = list(map(str, input().split()))
    bubble, selection = deepcopy(a), deepcopy(a)
    bubble = BubbleSort(bubble, N)
    selection = SelectionSort(selection, N)
    print(*bubble)
    print(isStable(bubble, bubble))
    print(*selection)
    print(isStable(selection, bubble))

