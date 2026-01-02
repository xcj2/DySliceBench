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


dp = [[0,0] for i in range(n)]

den = [0 for i in range(n)]

for i in range(n-2,-1,-1):
	if a[i] > a[i-1]:
		den[i-1] = 1
	else:
		break

po = [0 for i in range(n)]

for i in range(1,n):
	if a[i] < a[i-1]:
		po[i] = po[i-1]+1
	else:
		po[i] = po[i-1] 

now = a[0]
st = 0
for i in range(n):
	for j in range(i+1,n):
		if a[j] >= a[j-1]:
			1
		else:
			dp[i][0] = j-1
			break
	else:
		dp[i][0] = j
	for j in range(i+1,n):
		if a[j] <= a[j-1]:
			1
		else:
			dp[i][1] = j-1
			break
	else:
		dp[i][1] = j

lb = 0
hav = 0
mo = 1000

for i in range(n):
	if dp[i][0] == i:
		mo += hav * a[i]
		hav = 0
	if dp[i][1] == i:
		hav += mo // a[i]
		mo %= a[i]
		lb = a[i]
print(mo + lb * hav)