def MI():return map(int,input().split())
def LI():return list(MI())

# n,k,c=MI()
# s=input()

"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors[1:]

n=int(input())
l=[]

yakusuu=(make_divisors(n-1))

for k in range(2,min(10**6,n)+1):
    NN=int(n)
    while NN>=k:
        if NN%k==0:
            NN=NN//k
        else:
            NN=NN%k
    if NN==1:
        l+=k,

ll=(l+yakusuu+[n])

print(len(set(ll)))