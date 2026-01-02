def bubbleSort(A,N):
    flag = 1 #????????????????????£??????????????????????????????????????¨??????
    i = 0

    while flag:
        flag = 0
        for j in range(N-1,i,-1):
            if int(A[j][1]) < int(A[j-1][1]):
                tmp = A[j]
                A[j] = A[j-1]
                A[j-1] = tmp
                flag = 1
        i += 1
    return A


def selectionSort(A,N):
    for i in range(0,N-1):
        minj = i
        j=i+1
        for j in range(j,N):
            if int(A[j][1]) < int(A[minj][1]):
                minj = j
        tmp = A[minj]
        A[minj] = A[i]
        A[i] = tmp
    return A

def isStable(ori,sorted):
    for i in range(len(ori)-1):
        for j in range(i+1, len(ori)-1):
            for a in range(len(ori)):
                for b in range(a+1, len(ori)):
                    if ori[i][1] == ori[j][1] and ori[i] == sorted[b] and ori[j] == sorted[a]:
                        return 'Not stable'
    return 'Stable'

def output(A):
    for i in range(len(A)):  # output
        if i == len(A) - 1:
            print(A[i])
        else:
            print(A[i], end=' ')

if __name__ == '__main__':

    N = int(input())

    numbers = input().split(' ')
    n1 = numbers.copy()
    n2 = numbers.copy()

    A = bubbleSort(n1,N)

    output(A)
    print(isStable(numbers,A))

    B = selectionSort(n2,N)

    output(B)
    print(isStable(numbers, B))