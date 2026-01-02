def quicksort(A, p, r):
    if p < r:
        q = patation(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

def patation(A, p, r):
    x = int(A[r][1])
    i = p - 1
    for j in range(p, r):
        if int(A[j][1]) <= x:
            i += 1
            tmp = A[i]; A[i] = A[j]; A[j] = tmp
    tmp = A[i+1]; A[i+1] = A[r]; A[r] = tmp
    return i+1

def print_list(A):
    if A == B:
        print("Stable")
    else:
        print("Not stable")

    for line in A:
        print(line[0], line[1])

A = []
n = int(input())
for i in range(n):
    A.append(input().split())
B = sorted(A, key=lambda x: x[1])
p = 0; r = n - 1
quicksort(A, p, r)
print_list(A)

