#import math
#import copy
#import sys
#import bisect
#input = sys.stdin.readline
mod=10**9+7
def factorial(x): #階乗計算
    n=1
    for i in range(x):
        n=(n*(i+1))%mod
    return n

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
def lcm(a, b):
    return((a*b)//gcd(a,b))
def div(x): #約数配列
    div=[1]
    check=2
    while(x!=1 and check <= int(x**0.5)+2):
        if(x%check==0):
            div.append(check)
            while(x%check==0):
                x=x//check
        check+=1
    if x != 1:
      div.append(x)
    return div
def div2(x): #素因数分解配列
    div2=[]
    check=2
    while(x!=1 and check <= int(x**0.5)+2):
        while x%check==0:
            div2.append(check)
            x/=check
        check+=1
    if x != 1:
      div2.append(x)
    return div2

def main():
    n,m = map(int,input().split())    
    if abs(n-m)>1:
        print(0)
    else:
        a=max(n,m)
        b=min(n,m)
        if a>b:
            print((factorial(a)*factorial(b))%mod)
        else:
            ans=(factorial(a)**2)%mod
            print((2*ans)%mod)
main()