def show (nums):
    for i in range(len(nums)):
        if i!=len(nums)-1:
            print(nums[i],end=' ')
        else :
            print(nums[i])

def bubble(A):
    flag = True
    i = 0
    n = len(A)
    while(flag):
        flag = False
        for j in range(i+1,n)[::-1]:
            if A[j][1] < A[j-1][1]:
                A[j],A[j-1] = A[j-1],A[j]
                flag = True
        i += 1

def selection(A):
    n = len(A)
    for i in range(0,n):
        minj = i
        for j in range(i,n):
            if A[j][1] < A[minj][1]:
                minj = j
        if i != minj:
            A[i],A[minj] = A[minj],A[i]

n = int(input())
A = list(input().split())
B = A.copy()

bubble(A)
selection(B)

show(A)
print("Stable")
show(B)
if A == B:
    print("Stable")
else:
    print("Not stable")


