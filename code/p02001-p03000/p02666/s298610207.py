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

def uf_find(n,p):

    ufl = []

    while p[n] != n:
        ufl.append(n)
        n = p[n]

    for i in ufl:
        p[i] = n

    return n


def uf_union(a,b,p,rank,tsize):

    ap = uf_find(a,p)
    bp = uf_find(b,p)

    if ap == bp:
        return True
    else:

        if rank[ap] > rank[bp]:
            p[bp] = ap
            tsize[ap] += tsize[bp]
        elif rank[ap] < rank[bp]:
            p[ap] = bp
            tsize[bp] += tsize[ap]
        else:
            p[bp] = ap
            rank[ap] += 1
            tsize[ap] += tsize[bp]

        return False

mod = 10**9+7
N = int(input())
P = list(map(int,input().split()))
fac,inv = modfac(N+10,mod)

ans = 0

p = [i for i in range(N)]
rank = [1] * N
tsize = [1] * N

for i in range(N):

    if P[i] == -1:
        continue
    nex = P[i] - 1
    uf_union(i,nex,p,rank,tsize)

able = [True] * N
c = []
d = []

for i in range(N):

    if P[i] == -1:
        nowp = uf_find(i,p)
        c.append(tsize[nowp])
        able[nowp] = False

for i in range(N):

    if uf_find(i,p) == i and able[i]:
        d.append(tsize[i])


ans = 0
for i in c:
    ans += i
for i in d:
    ans += i-1
ans *= pow(N-1,len(c),mod)
ans %= mod

#print (ans)

#自分を選んで減る場合
for i in c:
    ans -= (i-1) * pow(N-1,len(c)-1,mod)
    ans %= mod

#互いに選んで減る場合

dp = [0] * (len(c)+1)
dp[0] = 1

for i in c:
    for j in range(len(c)-1,-1,-1):
        dp[j+1] += dp[j] * i
        #dp[j+1] %= mod
#print (c,dp)

for i in range(2,len(c)+1):

    ans -= dp[i] * fac[i-1] * pow(N-1,len(c)-i,mod)
    ans %= mod

print (ans % mod)


"""
連結成分で考える
全ての街が -1 以外を選んだ時、
最小数 + -1の数
-1同士が選ぶことを考える
-1同士が選んだ時のみ答えが1減る
そうでなければ変化なし？

連結成分に-1は1つ以下しかない？
→正しい

-1を含まない連結成分は分けておく
-1の連結成分同士が求め合えば、答えは-1される

a個含む & bこ含む
場合

a*b * (N-1)^(K-2)
引けばいい

自分の連結成分を求めるときも1減る
ループを作ると1減るんだ！



"""
