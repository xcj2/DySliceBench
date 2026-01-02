#べき乗関数powを使った逆元の計算(modinvよりもPythonでは高速、PyPyだと遅い)
def modinv(a,m):
    return pow(a,m-2,m)

#n以下の素数列挙(O(nlog(n))
def primes(n):
    ass = {}
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2,int(n**0.5)+1):
        if not is_prime[i]:
            continue
        #i**2から始めてOK
        for j in range(i*2,n+1,i):
            is_prime[j] = False
    for i in range(len(is_prime)):
        if is_prime[i]:
            ass[i] = 0
    return ass

#[[素因数,数]]を出力
def fctr1(n): 
    f = []
    c = 0
    for i in range(2,int(n**0.5)+2):
        while n%i == 0:
            c += 1
            n = n//i
        if c !=0:
            f.append([i,c])
            c = 0
    if n != 1:
        f.append([n,1])
    return f

N = int(input())
A = list(map(int,input().split()))

e = primes(10**6+7)
inv = 0
P = 10**9+7

for i in range(N):
    inv = (inv+modinv(A[i],P))%P
    l = fctr1(A[i])
    for j in range(len(l)):
        e[l[j][0]] = max(e[l[j][0]],l[j][1])

ans = 1
for k in e.keys():
    if e[k] != 0:
        for i in range(e[k]):
            ans = ans*k%P
ans = ans*inv%P

print(ans)
