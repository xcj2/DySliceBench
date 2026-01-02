from sys import stdout
printn = lambda x: stdout.write(str(x))
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

def f(k,p):
    if p<k:
        ret = 0
    if k==0:
        ret = 1
    elif k==1:
        ret = p*9
    elif k==2:
        ret = 9*9*p*(p-1)//2
    else:
        ret = 9*9*9*p*(p-1)*(p-2)//6
    #ddprint("f k {} p {} ret {}".format(k,p,ret))
    return ret

def g(k,p,n):
    #ddprint("g k {} p {} n {} called".format(k,p,n))
    if p==0 or p<k:
        return 0
    if k==0:
        ret = 1
    elif p==1:
        ret = n
    elif n<10**(p-1):
        ret = g(k,p-1,n)
    else:
        m = n//(10**(p-1))
        ret = g(k-1,p-1,n-m*(10**(p-1))) + (m-1)*f(k-1,p-1) + f(k,p-1)
    #ddprint("g k {} p {} n {} ret {}".format(k,p,n,ret))
    return ret

n = inn()
k = inn()
print(g(k,100,n))
