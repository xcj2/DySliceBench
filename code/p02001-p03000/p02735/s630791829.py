
def IsvalidStep(arr,row1,col1,row2,col2):
    if arr[row2][col2]=="#" and arr[row1][col1]==".":
        return 1
    return 0    

def solve(arr,matrix,n,m):
    maxx=0
    if n>0:
        if arr[0][0]=="#":
            matrix[0][0]=1
        for col in range(1,m):
            matrix[0][col]=matrix[0][col-1]
            if arr[0][col]=="#" and arr[0][col-1]==".":
                matrix[0][col]+=1

        for row in range(1,n):    
            matrix[row][0]=matrix[row-1][0]
            if arr[row][0]=="#" and arr[row-1][0]==".":
                matrix[row][0]+=1
          
        for row in range(1,n):
            for col in range(1,m):
                matrix[row][col]=min(matrix[row-1][col]+IsvalidStep(arr,row-1,col,row,col),matrix[row][col-1]+IsvalidStep(arr,row,col-1,row,col))
        return matrix[n-1][m-1]        



n,m=map(int,input().split())
arr=[int(0) for i in range(n)]
matrix=[int(0) for i in range(n)]
for i in range(n):
    arr[i]=list(input())
    matrix[i]=[int(0) for _ in range(m)]



print(solve(arr,matrix,n,m))       


"""
def solve(arr,n,m,row,col,count):
    if row>=n or col>=m:
        return 1e9
    elif row==n-1 and col==m-1:
        if arr[row][col]=="#":
            count+=1
        return count
    else:
        if arr[row][col]=="#":
            count+=1
        return min(solve(arr,n,m,row+1,col,count),solve(arr,n,m,row,col+1,count))        
"""
