import sys
import math
input = sys.stdin.readline
ceil = math.ceil

def main():
    def isok(z,val):##適宜変更
        return (z-val<=2*d)
    def bisect(ls,val): ##valの関数isok(x,val)がTrueとなる一番右のindex を返す 全部Falseなら-1
        ok = -1
        ng = len(ls)
        idx = (ok+ng)//2
        while ng-ok>1:
            num = ls[idx]
            if isok(num,val):
                ok = idx
            else:
                ng = idx
            idx = (ok+ng)//2
        return ok ##一番右のTrueのindex  Trueの個数はok+1こ

    n,d,a = map(int,input().split())
    mon = []
    for i in range(n):
        x,h = map(int,input().split())
        mon.append((x,h))
    mon.sort()
    keys = [ls[0] for ls in mon] #bisect用の配列

    damage = [0]*(n+1)
    ans = 0
    for i in range(n):
        x,h = mon[i]
        res = h-damage[i]
        if res>0:##体力が残ってたら
            c = ceil(res/a)
            ans+=c
            idx = bisect(keys,x) ##爆風が届くぎりぎりの位置
            if idx==-1:continue
            damage[i] +=a*c
            damage[idx+1] -=a*c
        damage[i+1] += damage[i]
    print(ans)
if __name__=="__main__":
    main()
