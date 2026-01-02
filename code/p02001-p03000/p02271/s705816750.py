def readinput():
    n = int(input())
    a = list(map(int,input().split()))
    q = int(input())
    m = list(map(int,input().split()))
    return n,a,q,m

def canmake(a,i):
    if(len(a)==1):
        if(a==i):
            return True
        else:
            return False

    for j in range(len(a)):
        ii = i-a[j]
        can=canmake(a[:j-1]+a[j+1:],ii) 
        if(can==True):
            return True
    return False   


def main(n,a,q,m):
    for i in m:
        ans=canmake(a,i)
        if(ans==True):
            print('yes')
        else:
            print('no')
    return

def solve(a,i,m):
    if(m==0):
        return True
    if(i>=len(a)):
        return False
    return solve(a,i+1,m) or solve(a,i+1,m-a[i])

def main2(n,a,q,m):
    for mm in m:
        ans=solve(a,0,mm)
        if(ans==True):
            print('yes')
        else:
            print('no')


def main3():
    global n
    global a
    n=int(input())
    a=list(map(int,input().split()))
    q=int(input())
    ms=list(map(int,input().split()))
    for m in ms:
        ans=solve2(0,m)
        if(ans==True):
            print('yes')
        else:
            print('no')

def solve2(i,m):
    global n
    global a
    if(m==0):
        return True
    if(i>=n):
        return False
    return solve2(i+1,m) or solve2(i+1,m-a[i])

def main4():
    n = int(input())
    a = list(map(int,input().split()))
    q = int(input())
    m = list(map(int,input().split()))

    S = [0]*(2**n)
    #print(S)
    for i in range(2**n):
        b=1
        for j in range(n):
            #print(i,j,bin(b),i&b)
            if ( i&b == b):
                S[i] += a[j]
            b*=2
    #print(S)

    for mm in m:
        if (mm in S):
            print('yes')
        else:
            print('no')



if __name__=='__main__':
    #n,a,q,m = readinput()
    main4()
