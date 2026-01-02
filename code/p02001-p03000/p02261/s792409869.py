import copy

n = int(input())
c = input().split()
bubble = copy.copy(c)
select = copy.copy(c)

def BubbleSort(C, N):
    for i in range(0, N):
        for j in range(N-1, i, -1):
            if int(C[j][1]) < int(C[j-1][1]):
                temp = C[j]
                C[j] = C[j-1]
                C[j-1] = temp
    return C

def SelectionSort(C, N):
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if int(C[j][1]) < int(C[minj][1]):
                minj = j
        temp = C[i]
        C[i] = C[minj]
        C[minj] = temp
    return C

BubbleSort(bubble, n)
SelectionSort(select, n)

print(*bubble)
print("Stable")
print(*select)

def isSame(C1, C2):
    for i in range(0, len(C1)):
        if C1[i] != C2[i]:
            return False
    return True

if isSame(bubble, select):
    print("Stable")
else:
    print("Not stable")
    
         

