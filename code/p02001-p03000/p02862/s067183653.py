def mod(n,p):
    return n % p
#ある数をAで割ったとき，その数をpで割ったときの余りを求めるのにかけるべき数を返す
def bunbo(A, p): 
    # p-2を2進数にする
    pp = p-2
    pb = list(str(format(pp, 'b')))
    # ひっくりかえす
    pb.reverse()
    # pbの要素の数lとして，A^1, A^2, A^4, A^8, ..., A^(2^l)をpで割った余りを求める
    lpp = [mod(A,p)]
    for _ in range(len(pb)-1):
        lpp.append(mod((lpp[-1] ** 2), p))
    # 必要なやつだけ足して，x=(A^(p-2)をpで割った余り)を求める
    x = 1
    for i in range(len(pb)):
        if pb[i] == '1':
            x *= lpp[i]
    return mod(x, p)

def nckp(n, k, p):
    # 0!, 1!, 2!, 3!, ..., n!をリストに入れる
    nk = [1]
    for i in range(1,n+1):
        nk.append(mod((nk[-1] * i), p))
    return mod((nk[n] * bunbo(nk[k], p) * bunbo(nk[n-k], p)),p)

X, Y = map(int,input().split())
if (2*X-Y) % 3 != 0 or (2*Y-X) % 3 != 0:
    print(0)
elif 2*X-Y < 0 or 2*Y-X < 0:
    print(0)
else:
    a = (2*Y-X) // 3
    b = (2*X-Y) // 3
    n = a + b
    k = a
    p = 1000000007
    print(nckp(n, k, p))