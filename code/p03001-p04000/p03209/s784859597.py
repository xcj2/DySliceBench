
m={}
def bits(n):
    if n in m:
        return m[n]
    elif n==0:
        m[n]=1
        return 1
    else:
        m[n]=((1+bits(n-1))*2+1)
        return m[n]
c={}
def pat(n):
    if n in c:
        return c[n]
    elif n==0:
        c[n]=1
        return c[n]
    else:
        c[n]=1+pat(n-1)*2
        return c[n]

def func(n, x):
    if n==0:
        return 1
    if x <=1:
        return 0
    elif x-1 <= bits(n-1):
        return func(n-1, x-1)
    elif x-1-bits(n-1)<=1:
        return pat(n-1)+1
    else:
        return pat(n-1)+1+func(n-1, x-1-bits(n-1)-1)

n, x = map(int, input().split())

#print (func(n, x))
print(func(n, x))
