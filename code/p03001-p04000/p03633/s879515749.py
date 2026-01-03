def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def gcd_l(A):
    if len(A) == 1:
        return A[0]
    x = gcd(A[0], A[1])
    if len(A) == 2:
        return x
    for i in range(2, len(A)):
        x = gcd(x, A[i])
    return x

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_l(A):
    if len(A) == 1:
        return A[0]
    x = lcm(A[0], A[1])
    if len(A) == 2:
        return x
    for i in range(2, len(A)):
        x = lcm(x, A[i])
    return x


N = int(input())
T = [int(input()) for _ in range(N)]
T = list(set(T))
T.sort()
N = len(T)
L = []
'''
for i in range(N):
    flag = 1
    for j in range(N-1, i, -1):
        if T[j] % T[i] == 0:
            flag = 0
            break
    if flag:
        L.append(T[i])

GCD = gcd_l(L)
ans = 1
for i in range(len(L)):
    ans *= L[i] // GCD
ans *= GCD
if len(L) == 1:
    ans = L[0]
'''
ans = lcm_l(T)
print(ans)
