def gcd(n,m):
    while n:
        m,n = n,m%n
    return m

N = int(input())
A = list(map(int,input().split()))

maxA = max(A)
B = [0]*(maxA+1)
for i in range(2,maxA+1):
    if B[i] == 0:
        B[i] = i
        for j in range(2*i,maxA+1,i):
            B[j] = i

soinsu = set()
a,b = 0,0

def pariwise():
    global N,A,soinsu,a,b
    for i in range(N):
        a = A[i]
        b = set()
        while a != 1:
            b.add(B[a])
            a //= B[a]
        for j in b:
            if j in soinsu:
                return False
            soinsu.add(j)
    return True

def setwise():
    global N,A,soinsu,a,b
    a = A[0]
    for i in range(1,N):
        a = gcd(a,A[i])
    return (a == 1)

if pariwise():
    print('pairwise coprime')
elif setwise():
    print('setwise coprime')
else:
    print('not coprime')
