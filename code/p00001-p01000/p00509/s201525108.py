import math
import random
import sys

def gcd(a,b):
    if a==b:
        return a
    if a>b:
        return gcd(b,a)
    if b%a==0:
        return a
    return gcd(b%a,a)

def rabin(n):
##    print(n)
    for t in range(100):
        x=random.randint(2,n-1)
       ## print(x)
        if gcd(n,x)!=1:
            return False
        if pow(x,n-1,n)!=1:
            return False
            
    return True



def main():

    x,y = map(int,input().split())
    if y<0:
        if x==1:
            print(11)
        else:
            for _ in range(2*x):
                print(9,end='')
            print()
        return
    
    r=10**x
    r-=1
    rr=10**(x-1)-1
    while r!=rr:
        s=str(r)
        c=str(y)
        t=s[::-1]
        
        w=int(s+c+t)
        
        if rabin(w):
            print(w)
            return
        r=r-1
##    print("nasi")
    for _ in range(x):
        print(9,end='')
    print(y,end='')
    
    for _ in range(x):
        print(9,end='')
    print()
    
if __name__ == '__main__':
    main()
