def gcd(n, m):
    # 最大公約数
    a = max(n,m)
    b = min(n,m)
    while b:
        a, b = b, a % b
    return a

# 約数
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors


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

A,B = map(int, input().split())
gcd = gcd(A,B)
divs = make_divisors(gcd)
# ps = getprime(gcd)
if len(divs)==1:
    print(1)
else:
    print(len(factorization(gcd))+1)