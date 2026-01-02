def mod_combination(n, k, mod):
    # nCk (mod m)
    def mod_permutation(n, k, mod):
        if n<=k:
            return 1
        else:
            return (n * mod_permutation(n-1,k,mod))%mod

    def mod_inv_permutation(k, mod):
        k, mod = int(k), int(mod)
        if k<=1:
            return 1
        else:
            return (pow(k,mod-2,mod) * mod_inv_permutation(k-1, mod))%mod

    return (mod_permutation(n,n-k,mod) * mod_inv_permutation(k, mod))%mod

N, M = map(int, input().split(" "))
X=[]
Y=[]
c=-1
K = 10 ** 9 + 7
i=2
while True:
    if M % i == 0:
        X.append(i)
        Y.append(0)
        c += 1
        while M % i == 0:
            M /= i
            Y[c] += 1

    if i==2:
        i += 1
    else:
        i += 2

    if i>M:
        break

    if i**2>M:
        X.append(M)
        Y.append(1)
        break

ret = 1
for i in Y:
    ret *= mod_combination(i+N-1, i, K)
    ret %= K

print (ret)