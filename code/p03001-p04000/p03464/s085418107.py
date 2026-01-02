
import numpy as np
import sys
sys.setrecursionlimit(100000)



def acinput():
    return list(map(int, input().split(" ")))



directions=np.array([[1,0],[0,1],[-1,0],[0,-1]])
directions = list(map(np.array, directions))

mod = 10**9+7


def factorial(n):
    fact = 1
    for integer in range(1, n + 1):
        fact *= integer
    return fact



def serch(x, count):
    #print("top", x, count)
            

    for d in directions:
        nx = d+x
        #print(nx)
        if np.all(0 <= nx) and np.all(nx < (H, W)):
            if field[nx[0]][nx[1]] == "E":
                count += 1 
                field[nx[0]][nx[1]] = "V"
                count = serch(nx, count)  
                continue
            if field[nx[0]][nx[1]] == "#":
                field[nx[0]][nx[1]] = "V"
                count = serch(nx, count)    
                 
    return count

def f(x):
    for i in range(K):
        x = x-x % A[i]
    return x

def bisect_search(f,val=0,l=0,r=10**6):

    #is_increase=(f(r)-f(l))>=0

    eps=10**(-5)
    while True:

        c=(l+r)//2
        print(l,c,r)
        input()
        if f(c)==val and f(c-1)!=val:
            return c
        #if f(c)-val < eps:
        #    return c

        if f(c)>val:
            r=c

        else:
            l=c
        
        if l==r:
            return False

def bisect_search_int(f,val=0,l=0,r=10**6,equal=False):
    #is_increase=(f(r)-f(l))>=0
    
    eps=10**(-5)
    if not equal:
        siki = "f(c) > val"
    else:
        siki = "f(c) >= val"

    while r-l>1:

        c=(l+r)//2
        
        if eval(siki,{"c":c,"f":f,"val":val}):
            r=c            
        else:
            l=c
        
        #if l==r:
        #    return False
    if f(l)!= f(c) and f(r)!=f(c):
        return False
    return l,r



K=int(input())
A=acinput()

R = 2+K*max(A)
#R=10**6

l,r=bisect_search_int(f, 2,0,R,equal=True)
if f(l)==2:
    resL=l
elif f(r)==2:
    resL=r
else:
    resL=-1

l, r = bisect_search_int(f, 2,0,R,equal=False)
#print(l,r,f(l),f(r))
if f(l) == 2:
    resR = l
elif f(r) == 2:
    resR = r
else:
    resR = -1

if resL>=0:
    print(resL,resR)
else:
    print(-1)


#for x in range(0,20):
#    print(x,f(x))
