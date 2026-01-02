
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

def cmb(n,m):
    ans=1
    for i in range(n,n-m,-1):
        ans*=i
    for i in range(1,m+1):
        ans //=i
    return ans





def resolve():
    N,M=map(int,input().split())
    ans=1
    md=10**9+7
    if M==1:
        print(1)
        return
    for i in factorization(M):
        nn=i[1]+N-1
        ans *= cmb(nn,i[1])
        ans %=  md

    print(ans)
if __name__ == "__main__":
    resolve()