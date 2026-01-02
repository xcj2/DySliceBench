def main():
    N = int(input())
    A = input().split()
    B = A.copy()
    
    A = BubbleSort(A, N)
    print(*A)
    print('Stable')
    B = SelectionSort(B, N)
    print(*B)
    if A == B:
        print('Stable')
    else:
        print('Not stable')

def BubbleSort(A, N):
    count = 0
    for i in range(N):
        for j in range(N-1,i,-1):
            if A[j][1] < A[j-1][1]:
                A[j], A[j-1] = A[j-1], A[j]
                count += 1
    return A

def SelectionSort(A, N):
    count = 0
    
    for i in range(N):
        mini = i
        for j in range(i,N):
            if A[j][1] < A[mini][1]:
                mini = j
        if A[i][1] > A[mini][1]:
            A[i], A[mini] = A[mini], A[i]
            count += 1
    return A

main()

