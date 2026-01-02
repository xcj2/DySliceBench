def deg(n):
    cnt = 0
    while n%2==0:
        cnt += 1
        n = n//2
    return cnt
def gcm(a,b):
    while b>0:
        a,b = b,a%b
    return a
def lcm(a,b):
    c = gcm(a,b)
    return (a//c)*b
N,M = map(int,input().split())
A = list(map(int,input().split()))
n = deg(A[0])
flg = 0
for i in range(1,N):
    if deg(A[i])==n:continue
    else:
        flg = 1
        break
if flg==1:
    print(0)
else:
    B = [A[i]//2**n for i in range(N)]
    b = B[0]
    for i in range(1,N):
        b = lcm(b,B[i])
    m = 2**(n-1)*b
    print((M+m)//(2*m))