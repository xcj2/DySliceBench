#coding: UTF-8

N = int(input())
A = input()
#A = list(map(int, input().split()))
IN1 = [None] * N
IN2 = [None] * N
i=0


for a in A.split():
    tmp = int(a.lstrip("SHCD"))
    IN1[i] = [tmp, i, a]
    IN2[i] = [tmp, i, a]
    i+=1

def BubbleSort(A,N):
    for i in range(N - 1):
        for j in range(N - 1, i,-1):
            if A[j][0] < A[j - 1][0]:
                tmp = A[j]
                A[j] = A[j - 1]
                A[j - 1] = tmp

def InsertionSort(A,N):
    for i in range(0,N):
        minj = i
        for j in range(i, N):
            if A[j][0] < A[minj][0]:
                 minj = j
        if i != minj:
            tmp = A[i]
            A[i] = A[minj]
            A[minj] = tmp

def StableCheck(A):
    tmp = [0,0]
    for t in A:
        if(tmp[1] > t[1]):
            if(tmp[0] == t[0]):
                return False
        tmp = t
    return True


BubbleSort(IN1,N)
InsertionSort(IN2,N)

for i in range(N - 1):
    print(IN1[i][2],end=' ')
print(IN1[N - 1][2])
if(StableCheck(IN1)):print("Stable")
else:print("Not stable")

for i in range(N - 1):
    print(IN2[i][2],end=' ')
print(IN2[N - 1][2])
if(StableCheck(IN2)):print("Stable")
else:print("Not stable")