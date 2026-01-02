def BubbleSort(C, N):
    for i in range(N):
        for j in range(N-1, i,-1):
            if C[j][1] < C[j-1][1]:
                C[j], C[j-1] = C[j-1], C[j]
    return C
                
                

def SelectionSort(C, N):
    #print(C)
    for i in range(N):
        minj = i
        for j in range(i, N):
            if C[j][1] < C[minj][1]:
                minj = j
        C[i], C[minj] = C[minj], C[i]
        #print(C)
    return C


def IsStable(A, B):
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            for a in range(len(B)):
                for b in range(a+1,len(B)):
                    if A[i][1] == A[j][1] and A[i] == B[b] and A[j] == B[a]:
                        return False
    return True
        
                
n = int(input())
a = input().split()
b = a.copy()
c = a.copy()
ans1 = []
ans2 = []
    
ans1 = BubbleSort(b, n)
print(*ans1)
if IsStable(a, ans1):
    print('Stable')
else:
    print('Not stable')

ans2 = SelectionSort(c, n)
print(*ans2)
if IsStable(a, ans2):
    print('Stable')
else:
    print('Not stable')
