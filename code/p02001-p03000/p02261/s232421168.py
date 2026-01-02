from operator import lt

def main():
    N = int(input())
    A = list(input().split(' '))

    Ab = bubbleSort(A[:], N, lambda a, b: int(a[1]) < int(b[1]))
    As = selectionSort(A[:], N, lambda a, b: int(a[1]) < int(b[1]))

    print(' '.join([str(a) for a in Ab]))
    print('Stable')

    print(' '.join([str(a) for a in As]))
    print('Stable' if Ab == As else 'Not stable')

def bubbleSort(A, N, comp=lt):
    flag = True

    while flag:
        flag = False

        for j in range(N-1, 0, -1):
            if comp(A[j], A[j-1]):
                A[j], A[j-1] = A[j-1], A[j]
                flag = True

    return A

def selectionSort(A, N, comp=lt):
    for i in range(0, N-1):
        minj = i

        for j in range(i, N):
            if comp(A[j], A[minj]):
                minj = j

        if i != minj:
            A[i], A[minj] = A[minj], A[i]

    return A

if __name__ == '__main__':
    main()