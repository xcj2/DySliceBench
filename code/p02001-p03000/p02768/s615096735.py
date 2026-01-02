def input_multiple_number():
    return map(int, input().split())

def cmb_mod(n,r,mod):
    x=1
    y=1
    if n/2<r:
        r=n-r
    for i in range(r):
        x*=n-i
        if x>mod:
            x%=mod
        y*=r-i
        if y>mod:
            y%=mod
    val=x*pow(y,mod-2,mod)%mod #pow(y,mod-2,mod)モジュラ逆数
    return val

def modulo(a,mod):
    return (a % mod + mod) % mod


n_given,a_given,b_given = input_multiple_number()

MOD = 10 ** 9 + 7
mod = MOD
ans = pow(2,n_given,MOD)

ans -= cmb_mod(n_given,a_given,mod)
ans -= cmb_mod(n_given,b_given,mod)


ans = modulo(ans,mod) - 1
print(ans)
