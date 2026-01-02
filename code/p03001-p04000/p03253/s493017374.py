def soinsuu(a):
    yy,j=[],2
    y=yy.append
    while(a>1):
        for i in range(j,int(a**0.5)+1):
            if a%i==0:
                y(i)
                a,j=a//i,i
                break
        else:
            y(a)
            break
    yy.sort()
    return yy

def n_func(n,mod=10**9+7):
    ans=1
    for i in range(1,n+1):ans=(ans*i)%mod
    return ans
def inv_n(n,mod=10**9+7):return pow(n,mod-2,mod)
def nCr(n,r,mod=10**9+7):return inv_n(n_func(n-r,mod)*n_func(r,mod)%mod,mod)*n_func(n,mod)%mod


def main():
    mod=10**9+7
    from collections import Counter
    n,m=map(int,input().split())
    s=Counter(soinsuu(m))
    ans=1
    for i in s.values():
        ans=(ans*nCr(n+i-1,i))%mod
    print(ans)
    
if __name__ == '__main__':
	main()