facs = []
M = 1000000007

def modulo(n):
    global facs
    facs = [1]*(n+1)
    last = 1
    for i in range(1,n+1):
        last = facs[i] = mulmod(last,i,M)
        
def mulmod(x,y,p):
    return x*y % p
def divmod(x,y,p):
    return mulmod(x,powmod(y,p-2,p),p)

def ncr(n,r):
    if n<r:
        return 0
    if n==r:
        return 1
    res = facs[n]
    res = divmod(res,facs[r],M)
    res = divmod(res,facs[n-r],M)
    return res

def powmod(x,y,p):
    if y==0:
        return 1
    elif y==1:
        return x % p
    elif (y%2)==0:
        return powmod(x,y//2,p)**2 % p
    else:
        return powmod(x,y//2,p)**2 * x % p

import sys
input = sys.stdin.readline

MAX= 2005
def resolve():
    n,k = map(int,input().split())
    red = n-k
    modulo(MAX)
    print(n-k+1)
    for i in range(2,k+1):
        if i>red+1:
            print(0)
        else:
            ans = 1
            if(red-i+1)>0:
                ans = ans * ncr(red+1,red-i+1)
            if(k-i)>0:
                ans = ans * ncr(k-1,k-i)
            print(ans%M)

if __name__ == "__main__":
    resolve()