def check(orijinal,A):
    A2 = [int(x[1]) for x in A]
    orijinal2 = [int(x[1]) for x in orijinal]
    B=[x for x in set(A2) if  A2.count(x)>1]
    flag=True
    if len(B)!=0:
        count=0
        soeji=[]
        for fig in B:
            a=[i for i, x in enumerate(orijinal2) if x == fig]
            b=[i for i, x in enumerate(A2) if x == fig]
            orijinal3=[orijinal[k] for k  in a]
            A3 = [A[k] for k in b]
            if orijinal3!=A3:
                flag=False
                break
    if flag:
        print("Stable")
    else:
        print("Not stable")
def selectSort(N,A):
    count=0
    orijinal=A[:]
    B=[ int(x[1]) for x in A]
    C=list(range(N))
    for i in range(N):
        min=i
        for j in range(i,N):
            if B[j] < B[min]:
                min=j
        if i<=min:
            count+=1
            # for k in range(N): print(A[k], end=' \n'[k + 1 == N])
            A[i],A[min]=A[min],A[i]
            B[i], B[min] = B[min], B[i]

    for k in range(N):print(A[k],end=' \n'[k+1==N])
    check(orijinal,A)



def bubbleSort(N,A):
    i=0
    flag=True
    count=0
    orijinal = A[:]
    B = [int(x[1]) for x in A]
    while flag:
        flag=False
        for j in range(N-1,i,-1):
            if B[j]<B[j-1]:#ソート必須
                A[j],A[j-1]=A[j-1],A[j]
                B[j], B[j - 1] = B[j-1], B[j]
                count+=1
                flag=True


        i += 1
    for i in range(N):print(A[i],end=' \n'[i+1==N])
    check(orijinal, A)

N=int(input())
A=[(x) for x in input().split()]
B=A[:]
bubbleSort(N,A)
selectSort(N,B)


