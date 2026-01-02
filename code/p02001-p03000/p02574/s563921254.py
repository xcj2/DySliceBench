N = int(input())
A = list(map(int, input().split()))
# N = 10**6
# A = [10**6-i for i in range(N)]

def is_pairwise_coprime():
    l = [0]*(10**6+1)
    for a in A:
        for j in range(2, int(a**(1/2))+2):
            if a % j == 0:
                if l[j]:
                    return False
                l[j] = 1
            while a % j == 0:
                a //= j
        if a != 1:
            if l[a]:
                return False
            l[a] = 1
    return True

def gcd(a, b):
    if a > b:
        a, b = b, a
    if a == 0:
        return b
    return gcd(a, b%a)

def is_setwise_coprime():
    A_gcd = A[0]
    for a in A[1:]:
        A_gcd = gcd(A_gcd, a)
        if A_gcd == 1:
            break
    return (A_gcd == 1)

if is_pairwise_coprime():
    print("pairwise coprime")
elif is_setwise_coprime():
    print("setwise coprime")
else:
    print("not coprime")