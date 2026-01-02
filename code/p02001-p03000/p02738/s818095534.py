
"""
Writer: SPD_9X2
https://atcoder.jp/contests/agc043/tasks/agc043_d

結局は、N個をX個の集合に、3個を最大として分ける通り数？
それを集合内降順ソートして、全体で昇順ソートしたものは構成可能

3こ取る集合の数、2個とる集合の数を決めれば、1この集合の数もわかる
→2重ループで解けそう

1ことるやつは、 全体C取る数
2ことるやつは、 残りC取るやつ　* (Π(i=1~N) 2i C 2) / (N!)
3ことるやつは　  ( Π(i=1~N) 3i C 3 ) / (N!)

Π(i=1~N) 2i C 2 = TX[i]
Π(i=1~N) 3i C 3 = TT[i]を各Nについて前計算しておく必要性あり

グループ内の最大が先頭である必要があるけど、残りは自由
→なんか違くね…

→2の個数が1の個数を超えたらダメなのか！！


もうちょっとちゃんと考察しよう
ある順列があっったとする。これが構築可能かの判定
→大小の塊をセットにする。

塊の大きさは3以下、かつ2の塊の数が1より多かったらダメ
このような分け方のとき、かならず構築できる？

1,2の大きさを組み合わせ、先頭が昇順になるように合わせればおｋ

"""
def inverse(a,mod): #aのmodを法にした逆元を返す
    return pow(a,mod-2,mod)



#modのn!と、n!の逆元を格納したリストを返す(拾いもの)
#factorialsには[1, 1!%mod , 2!%mod , 6!%mod… , n!%mod] が入っている
#invsには↑の逆元が入っている

def modfac(n, MOD):
 
    f = 1
    factorials = [1]
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    inv = pow(f, MOD - 2, MOD)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
    return factorials, invs


def modnCr(n,r,mod,fac,inv): #上で求めたfacとinvsを引数に入れるべし(上の関数で与えたnが計算できる最大のnになる)

    return fac[n] * inv[n-r] * inv[r] % mod


N,mod = map(int,input().split())

fac,inv = modfac(10*N+30,mod)

TX = [1]

for i in range(1,2 * N+10):
    
    TX.append(TX[-1] * modnCr(2*i,2,mod,fac,inv) % mod)

TT = [1]

for i in range(1,2 * N+10):
    
    TT.append(TT[-1] * modnCr(3*i,3,mod,fac,inv) % mod)

ans = 0

for tri in range(N+1):

    for sec in range(2*N):

        one = 3*N - 3*tri - 2*sec
        if one < 0 or one < sec:
            continue

        now = modnCr(3*N,one,mod,fac,inv)
        now *= modnCr(3*N-one,2*sec,mod,fac,inv) * TX[sec] * inv[sec]
        now *= TT[tri] * inv[tri] * pow(2,tri,mod)

        now %= mod
        ans += now
        #print (tri,sec,one,now)
        ans %= mod

print (ans)

        
