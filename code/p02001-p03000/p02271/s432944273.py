def exhaustive(i,A,m,n):
    if m==0:
        return True
    if i>=n:
        return False
    
    return exhaustive(i+1,A,m,n) or exhaustive(i+1,A,m-A[i],n)
    
    
def inputting():
    n=int(input())
    A=list(map(int,input().split()))
    q=int(input())
    M=list(map(int,input().split()))
    return n,A,q,M

def main():
    A=[]
    M=[]
    n,A,q,M=inputting()
    total = sum(A)
    for m in M:
        if total<m:
            print("no")
            continue
        bool=exhaustive(0,A,m,n)
        if bool==True:
            print("yes")
        else:
            print("no")

if __name__=='__main__':
    main()

