#import math
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
    n=int(input())
    a = list(map(int,input().split()))
    x={}
    for i in range(n):
        if a[i] not in x:
            x[a[i]]=1
        else:
            x[a[i]]+=1
    y=[]
    for i in x:
        if x[i]>=2:
            y.append(i)
            if x[i]>=4:
                y.append(i)
    y.sort(reverse=True)
    if len(y)>=2:
        print(y[0]*y[1])
    else:
        print(0)

main()