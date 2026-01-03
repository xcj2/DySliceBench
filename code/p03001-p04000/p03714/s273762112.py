import sys,collections as cl,bisect as bs,heapq as hq
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
	if len(x) == 0:
		return []
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

def pow_k(x, n):
    ans = 1
    while n:
        if n % 2:
            ans *= x
        x *= x
        n >>= 1
    return ans

"""
def nibu(x,n,r):
	ll = 0
	rr = r
	while True:
		mid = (ll+rr)//2

	if rr == mid:
		return ll
	if (ここに評価入れる):
		rr = mid
	else:
		ll = mid+1
"""


n = onem()

a = l()

fl = a[:n]
ba = a[2*n:]



ba = list(map(lambda x:-x,ba))

po = cl.deque(a[n:2*n])

hq.heapify(fl)
fll = fl
hq.heapify(ba)
baa = ba
al = [sum(fll),sum(baa)]
best = [[0,0] for i in range(n+1)]
best[0] = [al[0],0]
best[-1] = [0,al[1]]
for i in range(n):
	aaa = hq.heappop(fll)
	bbb = po[i]
	if bbb >= aaa:
		hq.heappush(fll,bbb)
		best[i+1][0] = al[0] - aaa + bbb
		al[0] += -aaa + bbb
	else:
		hq.heappush(fll,aaa)
		best[i+1][0] = al[0]

for i in range(n-1,-1,-1):
	aaa = hq.heappop(baa)
	bbb = -po[i]
	if aaa <= bbb:
		hq.heappush(baa,bbb)
		best[i][1] = al[1] - aaa + bbb
		al[1] += -aaa + bbb
	else:
		hq.heappush(baa,aaa)
		best[i][1] = al[1]

ans = -Max

for i in range(n+1):
	ans = max(ans,best[i][0]+best[i][1])

print(ans)