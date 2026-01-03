N = int(input())
le = [int(input()) for i in range(N)]
le.sort()#昇順
#３数以上の最小公倍数を求める問題
#a,b2数の最小公倍数とcの最小公倍数で求められる
#２数の最小公倍数はユークリッドの互除法を利用して再帰関数で求められる。

def GCD(a,b):
    if b == 0:
        return a
    return GCD(b,a%b)


def LCM(a,b):
    return int(a*b//GCD(a,b))

def multi_LCM(le):
    # print(le)
    if len(le)==1:
        return
    mxle=le[-1]
    del(le[-1])
    le[-1]=LCM(le[-1],mxle)
    multi_LCM(le)

if(len(le)==2):
    le[0]=LCM(le[0],le[1])
if(len(le)>=2):
    multi_LCM(le)

print(le[0])
