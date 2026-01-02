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
    if a==[0 for _ in range(n)]:
        print("Yes")
        exit()
    if n%3!=0:
        print("No")
        exit()
    else:
        a.sort()
        x=a[0]
        z=a[n-1]
        if n%2==0:
            y=a[n//2]
        else:
            y=a[((n+1)//2)-1]
        x0=y0=z0=0
        for i in range(n):
            if a[i]==x:
                x0+=1
            if a[i]==y:
                y0+=1
            if a[i]==z:
                z0+=1
        if x==0 and x0==n//3 and y==z:
            print("Yes")
            exit()
        if x0!=n//3 or y0!=n//3 or z0!=n//3:
            print("No")
            exit()
        cnt={}
        index=0
        while x != 0:
            if x//2>0:
                if x%2!=0:
                    if index not in cnt:
                        cnt[index]=1
                    else:
                        cnt[index]+=1
                x=x//2
                index+=1
            else:
                if index not in cnt:
                    cnt[index]=1
                else:
                    cnt[index]+=1
                x=0
        index=0
        while y != 0:
            if y//2>0:
                if y%2!=0:
                    if index not in cnt:
                        cnt[index]=1
                    else:
                        cnt[index]+=1
                y=y//2
                index+=1
            else:
                if index not in cnt:
                    cnt[index]=1
                else:
                    cnt[index]+=1
                y=0
        index=0
        while z != 0:
            if z//2>0:
                if z%2!=0:
                    if index not in cnt:
                        cnt[index]=1
                    else:
                        cnt[index]+=1
                z=z//2
                index+=1
            else:
                if index not in cnt:
                    cnt[index]=1
                else:
                    cnt[index]+=1
                z=0
        for i in cnt:
            if cnt[i]%2==1:
                print("No")
                exit()
        print("Yes")

main()