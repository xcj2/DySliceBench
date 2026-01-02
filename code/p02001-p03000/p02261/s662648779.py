n=int(input())
#A=list(map(int, input().split()))
B=list(input().split())
C=B.copy()

def bubblesort(A,n):
    #print(A)
    count=0
    flag=1
    while flag:
        flag=0
        for j in reversed(range(1,len(A))):
            if int(A[j][1])<int(A[j-1][1]):
                tmp=A[j-1]
                A[j-1]=A[j]
                A[j]=tmp
                flag=1
                count+=1
    return(A,count)

def selectsort(A,n):
    count=0
    for i in range(len(A)):
        minj=i
        #flag=0
        for j in range(i,len(A)):
            if int(A[j][1])<int(A[minj][1]):
                minj=j
                #flag=1
        if i!=minj:
            A[i],A[minj]=A[minj],A[i]
            count+=1
    #print(A)
    return(A,count)

#バブルソートの結果と比較する
def isStable(result1, result2):
    if result1 == result2:
        return True
    return False


result1,count1=bubblesort(B,n)
print(" ".join([str(i) for i in result1]))
print("Stable")
result2,count2=selectsort(C,n)
print(" ".join([str(i) for i in result2]))
if isStable(result1, result2) == True:
    print("Stable")
else:
    print("Not stable")

#print(count)

