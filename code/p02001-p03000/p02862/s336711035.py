from sys import setrecursionlimit
setrecursionlimit(4100000)

x, y = map(int, input().split())

mod = 1000000007
f = 0
df = abs(x-y)     #difference
tm = (x+y)//3   #time

if (x+y)%3 != 0:
    f = 1
elif tm < df:
    f = 1
else:
    pass

def mod_a_to_bth_power(a:int, b:int):
    if b%2 == 0:
        return (mod_a_to_bth_power(a, b//2)**2)%mod
    elif b == 1:
        return a%mod
    else:
        return ((mod_a_to_bth_power(a, b//2)**2)*a)%mod

def mod_inverse(a:int):
    return mod_a_to_bth_power(a, mod-2)

def mod_nCr(n:int, r:int):
    num, den = 1, 1 #numerator denominator
    for i in range(r):
        num = (num*(n-i))%mod
        den = (den*(i+1))%mod
    return (num*mod_inverse(den))%mod

if f == 1:
    print(0)
else:
    if df == 0:
        c = tm//2
    else:
        c = (tm-df)//2+df
    ans = mod_nCr(tm, c)
    print(ans)