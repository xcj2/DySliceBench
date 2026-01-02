N ,a,b= list(map(int,input().split(' ')))


M = 10**9+7

def pow(x,n):
    if n==0:
        return 1
    res = pow((x*x)%M,n//2)
    if (n%2)==1:
        res = (res*x)%M
    return res


def power(x,n):
    res = 1
    if(n>0):
        res = power(x,n//2)
        if (n%2)==0:
            res = (res*res)%M
        else:
            res = (((res*res)%M)*x)%M
    return res

def comb(n,a):
    ans = 1
    for i in range(a):
        ans = (ans*(n-i))%M
        ans = (ans*power(i+1,M-2))%M 
    return ans

#print(pow(10,2))
#print(power(5,8))

print((power(2,N)-1-comb(N,a)-comb(N,b))%M)