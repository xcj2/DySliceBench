def bSort(A):
    flag = 1
    i = 0
    count = 0
    while flag:
        flag = 0
        for j in range(len(A)-1, i, -1):
            if int(A[j][1]) < int(A[j-1][1]):
                tmp = A[j]
                A[j] = A[j-1]
                A[j-1] = tmp
                flag = 1
                count += 1
        i += 1
    return A, count

def sSort(A):
    count = 0
    for i in range(len(A)):
        minj = i
        for j in range(i, len(A)):
            if int(A[j][1]) < int(A[minj][1]):
                minj = j
        if minj != i:
            count += 1
        tmp = A[i]
        A[i] = A[minj]
        A[minj] = tmp
    return A, count

def isStable(input_a, output_a):
    for v1, v2 in zip(input_a, output_a):
        if v1 != v2:
            return 'Not stable'
    return 'Stable'

if __name__ == '__main__':
    length = input()
    data = input().split()
    sort_s, _= sSort(list(data))
    sort_b, _= bSort(list(data))
    print (' '.join([str(x) for x in sort_b]))
    print (isStable(sort_b, sort_b))
    print (' '.join([str(x) for x in sort_s]))
    print (isStable(sort_b, sort_s))
