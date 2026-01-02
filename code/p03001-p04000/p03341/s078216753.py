#import math
#import copy
#import sys
#import bisect
#input = sys.stdin.readline
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
def lcm(a, b):
    return((a*b)//gcd(a,b))
def div(x):#約数配列
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
def div2(x):#素因数分解配列
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
    #x,y = map(int,input().split())           x=1,y=2
    #a = input().split()                      a=['1','2','3',...,'n']
    #a = list(map(int,input().split()))       a=[1,2,3,4,5,...,n]
    #li = input().split('T')	              FFFTFTTFF => li=['FFF', 'F', '', 'FF']
    #複数行の「1 2 3 4」型の入力を一配列に
    #x = sorted([list(map(int, input().split())) for _ in range(n)])
    #ソート x.sort(key=lambda y:y[1])
    # print("Yes")  print("No")  x=[[0 for _ in range(n)] for _ in range(n)]
    n=int(input())
    s=list(input())
    m=n
    cnt=0
    for i in range(n-1):
        if s[i+1]=="E":
            cnt+=1
    m=min(m,cnt)
    for i in range(n-1):
        if s[i+1]=="E":
            cnt-=1
        if s[i]=="W":
            cnt+=1
        if m > cnt:
            m=cnt
    print(m)
main()