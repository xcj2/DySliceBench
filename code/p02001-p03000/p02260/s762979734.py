def selection_sort(A):
    count = 0
    for i in range(len(A)):
        mini = i
        for j in range(i, len(A)):
            if A[j] < A[mini]:
                mini = j
        count += swap(A, mini, i)
    print_array(A)
    return count


def swap(A, i, j):
    if i != j:
        tmp = A[j]
        A[j] = A[i]
        A[i] = tmp
        return 1
    else:
        return 0


def print_array(array):
    print(" ".join([str(x) for x in array]))


amount = int(input())
numbers = [0 for i in range(amount)]
numbers = list(map(int, input().split()))
count = selection_sort(numbers)
print(count)