n=int(input())
m=len(str(n))
k=int(input())
def c(n,m):
    import math
    if n-m<0 or m<=0:
        return 0
    return(math.factorial(n)//math.factorial(n-m)//math.factorial(m))
def f(m,k):
    return c(m,k)*9**(k)
#ans=f(m-1,k)
#ans+=f(m-1,k-1)*(int(str(n)[0])-1)

def slove(n,k):
    if k==0:
        return 0
    m=len(str(n))
    t=0
    t+=f(m-1,k)
    t+=f(m-1,k-1)*(int(str(n)[0])-1)
    if k==1:
        t+=int(str(n)[0])
    if n>9:
        t+=slove(int(str(n)[1:]),k-1)
    else:
        if k==1:
            return n
    return t

print(slove(n,k))
