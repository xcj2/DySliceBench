import sys,bisect as bs,collections as cl
sys.setrecursionlimit(100000)
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

a = list(input())
aa = s(a)

al = []
ppp = [0]
ans = sum(map(lambda x:x[1]-1,aa))
for i in range(len(aa)-1):
    ppp.append(ppp[-1]+aa[i][1])

if len(aa) != 1:
    al.append([aa[0][1],0,1])
    al.append([aa[-1][1],len(aa)-1,1])

for i in range(1,len(aa)-1):
    al.append([aa[i][1],i,2])
al.sort(key = lambda x:x[2],reverse = True)
on = [True for i in range(n)]
oon = [0 for i in range(len(aa))]
al = cl.deque(al)
co = min(len(aa),k)
while co:
    if len(al) == 0:
        break
    an = al.popleft()
    co -= 1
    if an[2] == 1:
        if an[1] == 0:
            if not oon[1] == -1:
                oon[0] = -1
                oon[1] = 1
                ans += 1
            else:
                co += 1
        else:
            if not oon[-2] == -1:
                oon[-1] = -1
                oon[-2] = 1
                ans += 1
            else:
                co += 1
    else:
        if not (oon[an[1]-1] == -1 or oon[an[1]+1]):
            oon[an[1]-1] = 1
            oon[an[1]+1] = 1
            oon[an[1]] = -1
            ans += 2
        else:
            co += 1

print(ans)




