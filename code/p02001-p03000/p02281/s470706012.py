#coding:UTF-8
def isRoot(point,A,n):
    for i in range(n):
        if A[i][1]==point or A[i][2]==point:
            return False
    return True

def isBranch(point,A,ans):
    if A[point][1]!=-1:
        ans.append(A[point][1])
        isBranch(A[point][1],A,ans)
    if A[point][2]!=-1:
        ans.append(A[point][2])
        isBranch(A[point][2],A,ans)
        
def isIn(point,A,ans):
    if A[point][1]!=-1:
        isIn(A[point][1],A,ans)
    ans.append(point)
    if A[point][2]!=-1:
        isIn(A[point][2],A,ans)

def isPost(point,A,ans):
    if A[point][1]!=-1:
        isPost(A[point][1],A,ans)
    if A[point][2]!=-1:
        isPost(A[point][2],A,ans)
    ans.append(point)
        
def Pre(A,n):
    ans=[]
    for i in range(n):
        if isRoot(A[i][0],A,n)==True:
            ans.append(A[i][0])
            if A[i][1]!=-1:
                ans.append(A[i][1])
                isBranch(A[i][1],A,ans)
            if A[i][2]!=-1:
                ans.append(A[i][2])
                isBranch(A[i][2],A,ans)
    print("Preorder")
    for i in range(n):
        ans[i]=str(ans[i])
    print(" "+" ".join(ans))

def In(A,n):
    ans=[]
    for i in range(n):
        if isRoot(A[i][0],A,n)==True:
            if A[i][1]!=-1:
                isIn(A[i][1],A,ans)
            ans.append(A[i][0])
            if A[i][2]!=-1:
                isIn(A[i][2],A,ans)
    print("Inorder")
    for i in range(n):
        ans[i]=str(ans[i])
    print(" "+" ".join(ans))

def Post(A,n):
    ans=[]
    for i in range(n):
        if isRoot(A[i][0],A,n)==True:
            if A[i][1]!=-1:
                isPost(A[i][1],A,ans)
            if A[i][2]!=-1:
                isPost(A[i][2],A,ans)
            ans.append(A[i][0])
    print("Postorder")
    for i in range(n):
        ans[i]=str(ans[i])
    print(" "+" ".join(ans))
    
def TW(A,n):
    Pre(A,n)
    In(A,n)
    Post(A,n)


if __name__=="__main__":
    n=int(input())
    A=[]
    for i in range(n):
        A.append(list(map(int,input().split(" "))))
    for i in range(n):
        minj=i
        for j in range(i,n):
            if A[j][0]<A[minj][0]:
                minj=j
        A[i],A[minj]=A[minj],A[i]
    TW(A,n)