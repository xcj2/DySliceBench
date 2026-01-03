#import math
#import copy
#import sys
#import bisect
#input = sys.stdin.readline
mod=10**9+7
def swap(a,b):
    c=a
    a=b
    b=c
    return a,b
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
    # x,y = map(int,input().split())           x=1,y=2
    # a = input().split()                      a=['1','2','3',...,'n']
    # a = list(map(int,input().split()))       a=[1,2,3,4,5,...,n]
    # li = input().split('T')	              FFFTFTTFF => li=['FFF', 'F', '', 'FF']
    # 複数行の「1 2 3 4」型の入力を一配列に
    # x = sorted([list(map(int, input().split())) for _ in range(n)])
    # ソート x.sort(key=lambda y:y[1])
    # [chr(i) for i in range(97, 97+26)] 英語小文字リスト
    # [chr(i) for i in range(65, 65+26)] 英語大文字リスト atcoder
    # ord(c) chr(2) alphabet <=> number
    n=int(input())
    a = list(map(int,input().split()))
    ans=1
    k=0
    a.sort()
    for i in range(n-1):
        k+=a[i]
        if k*2>=a[i+1]:
            ans+=1
        else:
            ans=1
    print(ans)

main()