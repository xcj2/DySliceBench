def Int():
    return int(input())
def Ints():
    return map(int,input().split())
def IntList():
    return list(Ints())
def IntMat(N):
    return [IntList() for i in range(N)]

N,K = Ints()

mod = 10**9+7

One = [1,1]
R = 1

def divisor(M):
    A = []
    for i in range(1,int(M**0.5)+1):
        if M%i == 0:
            A.append(i)
            if M//i !=  i:
                A.append(M//i)
    #A.sort()
    return A

for i in range(2,K+1):
    tmp = 0
    tmp += pow(i,N,mod)
    tmp -= pow(i-1,N,mod)
    #print(divisor(i))
    for j in divisor(i):
        if j!=i:
            tmp -= One[j]
    #R += tmp%mod
    #R %= mod
    One.append(tmp%mod)
#print(One)
ans = 0
Rone = [0]
for i in range(1,K+1):
    Rone.append((Rone[-1]+One[i])%mod)

#print(Rone)
for i in range(1,K+1):
    ans += i*Rone[K//i]
    ans %= mod
print(ans)