import math

n=int(input())
a=[int(i) for i in input().split()]
a.sort()

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


def setwise_coprime(a):
    b=a.copy()
    one=b.pop()
    for i in range(n-1):
        two=b.pop()
        one=math.gcd(one,two)
    if one==1:
        return True
    return False

def pairwise_coprime(an):
    frui=[0]*(10**6+1)
    for a in an:
        if a==1:
            continue
        soinnsuu_list=factorization(a)
        for i in soinnsuu_list:
            if frui[i]==1:
                return False
            for k in range(1,int(10**6/i)+1):
                frui[i*k]=1
    return True


if pairwise_coprime(a):
    print("pairwise coprime")
elif setwise_coprime(a):
    print("setwise coprime")
else:
    print("not coprime")
