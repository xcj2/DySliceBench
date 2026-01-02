import copy
def selection_sort(A):
    global c
    c=0 
    for i in range(0,len(A)-1):
        selection(A,i)
        
        
    return A

def selection(A,i):
    global c
    min=i
    for j in range(i+1,len(A)):
        if A[min][1]>A[j][1]:
            min=j
            
            
    A[i],A[min]=A[min],A[i]
    if not A[i]==A[min]:
        c+=1
    
def bubble_sort(A):
    for i in range(0,len(A)-1):
        bubble(A,i)
        
    return A

def bubble(A,i):
    for j in range(0,len(A)-1-i):
        if A[j][1]>A[j+1][1]:
            A[j],A[j+1]=A[j+1],A[j]
            
            
def is_stable(A, B):
    for i in range(len(B) - 1):
        if B[i][1] == B[i + 1][1]:
            if A.index(B[i]) > A.index(B[i + 1]):
                return 'Not stable'
    return 'Stable'



n=int(input())
A=input().split()
A_t=[(i[0],int(i[1])) for i in A]
A_t2=copy.copy(A_t)
B_t=bubble_sort(A_t)
B=[i[0]+str(i[1]) for i in B_t]
print(' '.join(B))
print(is_stable(A_t,B_t))

S_t=selection_sort(A_t2)
S=[i[0]+str(i[1]) for i in S_t]

print(' '.join(S))
print(is_stable(A_t,S_t))
