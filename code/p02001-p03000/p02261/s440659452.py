def to_int(A):
    return int(A[1])

def bubble_sort(N, A):
    for i in range(N):
        for j in range(i+1, N)[::-1]:
            if to_int(A[j]) < to_int(A[j-1]):
                aj = A[j]
                A[j] = A[j-1]
                A[j-1] = aj
    return A

def selection_sort(N, A):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if to_int(A[j]) < to_int(A[minj]):
                minj = j
        a = A[i]
        A[i] = A[minj]
        A[minj] = a
    return A

def is_stable(bubble, selection):
    if bubble == selection:
        return "Stable"
    else:
        return "Not stable"

if __name__ == "__main__":
    N = int(input())
    A = input().split(" ")
    bubble = bubble_sort(N, A[:])
    selection = selection_sort(N, A[:])
    print(" ".join(bubble))
    print("Stable")
    print(" ".join(selection))
    print(is_stable(bubble, selection))

