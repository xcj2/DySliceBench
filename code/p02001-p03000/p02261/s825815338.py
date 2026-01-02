def print_list(array):
    for i,e in enumerate(array):
        if i == N - 1:
            print(e)
        else:
            print(e, end=" ")

def bubbleSort():
    for i in range(N-1):
        for j in range(N-1, i, -1):
            if int(A[j][1:]) < int(A[j-1][1:]):
                w = A[j]; A[j] = A[j-1]; A[j-1] = w

def selectionSort():
    for i in range(N):
        min_index = i
        for j in range(i, N):
            if int(B[min_index][1:]) > int(B[j][1:]):
                min_index = j
        if i != min_index:
            w = B[i]; B[i] = B[min_index]; B[min_index] = w

N = int(input())
A = input().split()
B = list(A)
bubbleSort()
print_list(A)
print("Stable")
selectionSort()
print_list(B)
if A == B:
    print("Stable")
else:
    print("Not stable")

