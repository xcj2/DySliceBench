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
    
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a 
def multiple_gcd(a):
    ans = a[0]
    for i in range(1, len(a)):
        ans = gcd(ans, a[i])
    return ans

def pairwise_coprime_gcd():
    for i in range(N-1):
        for j in range(i+1, N):
            if gcd(A[i], A[j]) != 1:
                return 0
    return 1
def pairwise_coprime(A):
    prime = set()
    for i in range(N):
        fact = factorization(A[i])
        for x in fact:
            if x[0] in prime:
                return 0
            if x[0] != 1:
                prime.add(x[0])
    return 1

N = int(input())
A = list(map(int, input().split()))

if pairwise_coprime(A) == 1:
    print('pairwise coprime')
elif multiple_gcd(A) == 1:
    print('setwise coprime')
else:
    print('not coprime')
