A=[list(map(int,input().split())) for i in range(3)]
N=int(input())
B=[int(input()) for i in range(N)]
for b in B:
    for i in range(3):
        if b in A[i]:
            A[i][A[i].index(b)]=0
            
a=[]
            
def tate(X,i,c):
    cnt=0
    for j in range(3):
        if X[j][i]==0:
            cnt+=1
        if cnt==3:
            return c.append(1)
        
def yoko(X,i,c):
    cnt=0
    for j in range(3):
        if X[i][j]==0:
            cnt+=1
        if cnt==3:
            return c.append(1)
        
def naname(X,c):
    cnt=0
    for i in range(3):
        if X[i][i]==0:
            cnt+=1
        if cnt==3:
            return c.append(1)

def naname2(X,c):
    cnt=0
    for i in range(3):
        if X[i][2-i]==0:
            cnt+=1
        if cnt==3:
            return c.append(1)

            
for i in range(3):
    tate(A,i,a)
    yoko(A,i,a)
naname(A,a)
naname2(A,a)
    
if len(a)==0:
    print("No")
else:
    print("Yes")
    
