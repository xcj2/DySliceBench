from functools import reduce
import math
def gcd(x,y):
    if x%y==0:
        return y
    else:
        return (gcd(y, x%y))

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append(i)

    if temp!=1:
        arr.append(temp)

    if arr==[]:
        arr.append(n)

    return arr

def ans(n, a):
    div = {}
    for i in range(n):
        k = (factorization(a[i]))
        for j in k:
            if j==1:
                pass
            elif j not in div:
                div[j]=1
            else:
                return True
    return False
    

n = int(input())
a = list(map(int, input().split()))
gcd = reduce(math.gcd, a)
if gcd !=1:
    print("not coprime")
else:
    if ans(n, a):
        print("setwise coprime")
    else:
        print("pairwise coprime")
