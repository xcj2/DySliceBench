## coding: UTF-8
## coding: UTF-8
#N, M, K = 9, 3, 4
#N, M, K = map(int,input().split())
#N = 7
N = int(input())
mod = 10 ** 9 + 7
p = 10 ** 9 + 7


# 返り値: a と b の最大公約数
# 返り値: ax + by = gcd(a, b) を満たす (x, y) が格納される
def aug_gcd(a, b):
    lq = []
    while b > 0:
        q = int(a/b)
        r = a % b
        a = b
        b = r
        lq.append(q)
    x = 1
    y = 0
    for i in range(len(lq)):
        tmp = x
        x = y
        y = tmp - lq[(-1)*(i+1)] * y
    return a, x, y

#拡張ユークリッドの互除法による逆元計算
#拡張ユークリッドの方が二分累乗法より高速/mが素数でなくとも良い
def modinv(a, p):
    inv = aug_gcd(a, p)[1] #ax == 1(mod p) <==> ax + py == 0, xの値が逆元
    if(inv < 0):
        inv += p #pがマイナスだったらプラスに書き換える
    return inv


#[NC0, NC1, NC2, NC3, ..., NCN % p]
def N_Combination_k(N, p):
    #NCkのリストを作ります
    l = [1]
    res = 1
    for i in range(1, N+1):
        res *= (N+1-i)
        res %= p
        res *= modinv(i, p)
        res %= p
        l.append(res)
    return l

number_terms = N // 3
ret = 0
for i in range(1, number_terms+1):
    #print(i, )
    tmp = N_Combination_k(N-2*i-1, p)
    #print(tmp, tmp[i-1])
    ret += tmp[i-1]
    ret %= p
print(ret)