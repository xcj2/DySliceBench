def bubbleSort(A, N):
    flag = True
    while flag:
        flag = False
        for j in range(N-1,0,-1):
            if A[j][-1:] < A[j-1][-1:]:
                A[j],A[j-1] = A[j-1],A[j]
                flag = True
    return A

def selectionSort(A, N):
    for i in range(N):
        minj = i
        for j in range(i,N):
            if A[j][-1:] < A[minj][-1:]:
                minj = j
        if A[i][-1:] != A[minj][-1:]:
            A[i],A[minj] = A[minj],A[i]
    return A
    
def isStable(st,list2):
    for i in range(1,len(st)):
        if list2[i][-1:] == list2[i-1][-1:]:
            if st[i] != list2[i]:
                return "Not stable"
    return "Stable"
    
num = int(input())
li1 = input().split()
stli = bubbleSort(li1[:],num)
li2 = bubbleSort(li1[:],num)
print(*li2,sep=" ")
print(isStable(stli,li2))
li3 = selectionSort(li1[:],num)
print(*li3,sep=" ")
print(isStable(stli[:],li3))
