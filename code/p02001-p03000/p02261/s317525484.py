def bubblesort(A, N):
    for i in range(N):
        for j in range(N-1,i,-1):
            if A[j-1][1] > A[j][1]:
                A[j-1], A[j] = A[j], A[j-1]
    print(*A)
    return A
    
def selectionsort(A, N):
    for i in range(N):
        minj = i
        for j in range(i+1,N):
            if A[minj][1] > A[j][1]:
                minj = j
        A[minj], A[i] = A[i], A[minj]
    print(*A)
    return A
def judge(A,B,N):
    stable = True
    for m in range(N):
        for n in range(m+1, N):
            for x in range(N):
                for y in range(x+1,N):
                    if A[m][1]==A[n][1] and A[m]==B[y] and A[n]==B[x]:
                        stable = False
    if stable:
        return "Stable"
    else:
        return "Not stable"

N = int(input())
A = list(map(str, input().split(" ")))
B = A.copy()
Bubble = bubblesort(B,N)
print(judge(A,Bubble, N))
B = A.copy()
Selection = selectionsort(B,N)
print(judge(A,Selection, N))

