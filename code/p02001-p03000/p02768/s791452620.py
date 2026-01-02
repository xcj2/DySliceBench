MOD = 10 ** 9 + 7

n,a,b = map(int,input().split())

def pow_k(x, n):
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K = K * x % MOD
        x = x ** 2 % MOD
        n //= 2

    return K * x % MOD

def kai(x):
    an = 1
    for i in range(1,x+1):
        an = an * i % MOD
        
    return an

def kai2(x,yy):
    an = 1
    for i in range(x+1-yy,x+1):
        an = an * i % MOD
        
    return an

x = pow_k(2,n) - 1

mia = (kai2(n,a) * pow_k(kai(a),MOD-2)) % MOD
mib = (kai2(n,b) * pow_k(kai(b),MOD-2)) % MOD

ans = (4*MOD + x - mia - mib) % MOD

print(ans)