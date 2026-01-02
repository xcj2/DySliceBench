#coding:UTF-8
def BS(N,A):
    for i in range(N):
        for j in reversed(range(i+1,N)):
            if int(A[j][1:])<int(A[j-1][1:]):
                swap=A[j]
                A[j]=A[j-1]
                A[j-1]=swap
    return A

def SS(N,A):
    for i in range(N):
        minj=i
        for j in range(i,N):
            if int(A[j][1:]) < int(A[minj][1:]):
                minj=j
        
        swap=A[i]
        A[i]=A[minj]
        A[minj]=swap
    return A

def Stable(A1,A2):
    ans="Stable"
    for i in range(len(A1)):
        if A1[i][1:]==A2[i][1:] and A1[i][:1]!=A2[i][:1]:
            ans="Not stable"
    return ans

def SS2(N,A,B):
    A1=BS(N,A)
    print(" ".join(A1))
    print("Stable")
    A2=SS(N,B)
    print(" ".join(A2))
    print(Stable(A1,A2))

if __name__=="__main__":
    N=int(input())
    a=input()
    A=a.split(" ")
    B=a.split(" ")
    SS2(N,A,B)