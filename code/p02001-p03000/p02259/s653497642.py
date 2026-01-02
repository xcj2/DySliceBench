def print_list(A):
    print(" ".join(map(str, A)))

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def bubble(A):
    N = len(A)
    sorted = False
    count = 0
    for i in range(N):
        if (sorted):
            break
        sorted = True
        for j in reversed(range(i + 1, N)):
            if A[j] < A[j - 1]:
                swap(A, j, j - 1)
                count += 1
            sorted = False
    print_list(A)
    print(count)
    

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    bubble(A)
