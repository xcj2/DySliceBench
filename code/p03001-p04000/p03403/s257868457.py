import math
import copy
import sys
import bisect
input = sys.stdin.readline
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
    n=int(input())
    a = list(map(int,input().split()))
    a.append(0)
    x=[abs(a[0])]
    for i in range(n):
        x.append(abs(a[i]-a[i+1]))
    y=[abs(a[1])]
    for i in range(n-1):
        y.append(abs(a[i]-a[i+2]))
    S=sum(x)
    for i in range(n):
        print(S-x[i]-x[i+1]+y[i])

main()