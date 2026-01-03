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

def main():
    #x,y = map(int,input().split())	x=1,y=2
    #a = input().split()	a=['1','2','3',...,'n']
    #a = list(map(int,input().split()))	a=[1,2,3,4,5,...,n]
    #li = input().split('T')	FFFTFTTFF => li=['FFF', 'F', '', 'FF']
    #複数行の「1 2 3 4」型の入力を一配列に
    #x = sorted([list(map(int, input().split())) for _ in range(n)])
    #ソート x.sort(key=lambda y:y[1])
    # print("Yes")  print("No")  
    n,c,k = map(int,input().split())
    t=[]
    for i in range(n):
        t.append(int(input()))
    t.sort()
    ans=1
    x=[0,t[0]+k]
    for i in range(n):
        if x[0]==c:
            ans+=1
            x=[1,t[i]+k]
        elif t[i]<=x[1]:
            x[0]+=1
            if x[1]>t[i]+k:
                x[1]=t[i]+k
        else:
            ans+=1
            x=[1,t[i]+k]
    print(ans)
main()