def main():
    a=inputList()
    n=a[0]
    k=a[1]

    blue=k
    red=n-k

    for i in range(1,k+1):
        print(solve(red,blue,i))


def solve (red,blue,i):
    if(red<i-1):
        return 0

    ans=comb(red+1,i)*comb(blue-1,i-1)
    return ans%(10**9+7)

def comb(a,b):
    if(a-b<0):
        return 0
    if(a==b):
        return 1

    ans=1
    b=min(b,a-b)
    for i in range(b):
        ans*=a-i
        ans//=i+1

    ans %=10**9+7

    return ans


def inputList():
    a=list(map(int,input().split()))
    return a

def multisort(li,index):
    return sorted(li,key=lambda x: x[index])

if(__name__=='__main__'):
    main()