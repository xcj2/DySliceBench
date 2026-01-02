def sn(a):
    return ord(a) - ord("a")

def isok(idx,prev):##適宜変更
    return prev>=idx+n*loops


def bisect(ls,val): ##valの関数isok(x,val)がTrueとなる一番右のindex を返す 全部Falseなら-1
    ok = -1
    ng = len(ls)
    x = (ok+ng)//2
    while ng-ok>1:
        num = ls[x]
        if isok(num,val):
            ok = x
        else:
            ng = x
        x = (ok+ng)//2
    return ok ##一番右のTrueのindex  Trueの個数はok+1こ

S = input()
T = input()
lt = list(T)
ls = list(S)
set_s = set(list(S))
set_t = set(lt)
if not set_t <= set_s:
    print(-1)
    exit()
cnts = [[] for i in range(26)]
cnts_idx = [0]*26
for i,w in enumerate(ls):
    cnts[sn(w)].append(i)

loops = 0
n = len(S)
prev = -1
for t in lt:
    idx = bisect(cnts[sn(t)],prev)+1
    if idx==len(cnts[sn(t)]):
        loops+=1
        idx = 0
    prev = cnts[sn(t)][idx] + loops*n

print(prev+1)
