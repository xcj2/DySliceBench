A, B, C, D = map(int,input().split())

# A以上B以下の整数のうち、(CまたはDの倍数)でないものの個数を求める
# CまたはDの倍数の個数 = Cの倍数の個数+Dの倍数の個数-CとDの最小公倍数の倍数の個数
# 途中式でfloatが出てこないようにしないと大きな数の計算時に結果がズレるので注意

def ceil(x,y):
    if x%y == 0:
        return x//y
    else:
        return x//y+1

def n_multiple(x):
    return B//x - ceil(A,x) + 1

def lcd(x,y):
    while y>0:
        x,y = y, x%y
    return(x)

def gcd(x,y):
    return x*y//lcd(x,y)

print(int((B-A+1) - (n_multiple(C)+n_multiple(D)-n_multiple(gcd(C,D)))))