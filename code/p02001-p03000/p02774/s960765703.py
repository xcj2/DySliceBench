import sys,collections as cl,bisect as bs
sys.setrecursionlimit(100000)
input = sys.stdin.readline
mod = 10**9+7
Max = sys.maxsize
def l(): #intのlist
    return list(map(int,input().split()))
def m(): #複数文字
    return map(int,input().split())
def onem(): #Nとかの取得
    return int(input())
def s(x): #圧縮
    a = []
    aa = x[0]
    su = 1
    for i in range(len(x)-1):
        if aa != x[i+1]:
            a.append([aa,su])
            aa = x[i+1]
            su = 1
        else:
            su += 1
    a.append([aa,su])
    return a
def jo(x): #listをスペースごとに分ける
    return " ".join(map(str,x))
def max2(x): #他のときもどうように作成可能
    return max(map(max,x))
def In(x,a): #aがリスト(sorted)
    k = bs.bisect_left(a,x)
    if k != len(a) and a[k] ==  x:
        return True
    else:
        return False


n,k = m()

a = l()

a.sort()

po = bs.bisect(a,0)

a,b = a[po:],a[po-1::-1]

n,m = len(a),len(b)

ok = 10 ** 18

bad = - ok

while ok - bad > 1:
    x = (ok + bad)//2
    s = 0
    if x >= 0:
        s += n*m
        t = 0
        i = n
        for y in a:
            while i and a[i-1] * y > x:
                i -= 1
            t+= i
            if y*y <= x:
                t-=1
        s += t // 2
        t = 0
        i = m
        for y in b:
            while i and b[i-1] * y> x:
                i -= 1
            t += i
            if y * y <= x:
                t -= 1
        s += t//2
    else:
        i = m
        for y in a:
            while i and b[i-1] * y <= x:
                i -= 1
            s += m-i
    if s >= k:
        ok = x
    else:
        bad = x
print(ok)



