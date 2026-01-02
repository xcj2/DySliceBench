import copy
def BubbleSort(C, N) :
    for i in range(N-1) :
        for j in range(N-1, i, -1) :
            if C[j][1] < C[j-1][1] :
                C[j], C[j-1] = C[j-1], C[j]
    return(C)

def SelectionSort(C, N) :
    for i in range(N) :
        minj = i
        for j in range(i, N) :
            if C[j][1] < C[minj][1] :
                minj = j
        C[i], C[minj] = C[minj], C[i]
    return(C)

def Stable(A, B, N) :
    for i in range(N) :
        for j in range(i+1, N) :
            for a in range(N) :
                for b in range(a+1, N) :
                    if A[i][1] == A[j][1] and A[i] == B[b] and A[j] == B[a] :
                        return "false"
    return "true"

N = int(input())
OrgC = list(map(str, input().split()))
BubC = copy.copy(OrgC)
SelC = copy.copy(OrgC)
print(" ".join(BubbleSort(BubC, N)))
if Stable(OrgC, BubC, N) == "false" :
    print("Not stable")
else :
    print("Stable")

print(" ".join(SelectionSort(SelC, N)))
if Stable(OrgC, SelC, N) == "false" :
    print("Not stable")
else :
    print("Stable")


