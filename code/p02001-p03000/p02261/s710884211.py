def bubblesort_re(A,N):
    count = 0
    #A[i] > A[i+1]の状態がある→交換する必要がある：flag = True
    #交換する必要が無いとbreak→値の無駄な比較をしない
    flag = True
    while flag:
        flag = False
        # for i in range(N-1):
        #     if A[i][1] > A[i+1][1]:
        #         A[i],A[i+1] = A[i+1],A[i]
        #         count += 1
        #         flag = True
        for i in range(N-1,0,-1):
            if A[i][1] < A[i-1][1]:
                A[i],A[i-1] = A[i-1],A[i]
                count += 1
                flag = True

    return A,count

def min_index(A):
    index = 0
    m = A[0][1]
    for i in range(1,len(A)):
        if A[i][1] < m:
            m = A[i][1]
            index = i

    return index

# def selectionsort(A,N):
#     count = 0
#     for i in range(N-1):
#         j = min_index(A[i+1:])
#         if int(A[i][1]) > int(A[i+j+1][1]):
#             A[i],A[i+j+1] = A[i+j+1],A[i]
#             count += 1
#
#     return A,count

def selectionsort(A,N):
    count = 0
    for i in range(N):
        minj = i
        #最小値を見つけるfor文：O(n)
        for j in range(i+1,N):
            if A[j][1] < A[minj][1]:
                minj = j
        A[i],A[minj] = A[minj],A[i]

    return A,count

if __name__ == '__main__':
    import copy

    N = int(input())
    A = input().split()

    X = A.copy()
    s,t = bubblesort_re(X,N)
    for i in range(N):
        if i != N - 1:
            print(s[i],end = " ")
        else:
            print(s[i])
    print("Stable")

    X = A.copy()
    u,v = selectionsort(X,N)
    for i in range(N):
        if i != N - 1:
            print(u[i],end = " ")
        else:
            print(u[i])
    if s == u:
        print("Stable")
    else:
        print("Not stable")

