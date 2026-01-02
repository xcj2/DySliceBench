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

n,k = m()

a = l()
dp = [0 for i in range(n)]
ans = [0 for i in range(n)]
for i in range(min(50,k)):
	for j in range(n):
		po = a[j]
		if j - po < 0:
			dp[0] += 1
		else:
			dp[j-po] += 1
		if j + po + 1 <= n-1:
			dp[j+po+1] -= 1
	a[0] = dp[0]
	for j in range(1,n):
		dp[j] += dp[j-1]
		a[j] = dp[j]
	for j in range(n):
		dp[j] = 0

if k <= 50:
	print(jo(a))
	exit()

for j in range(n):
	a[j] += k-51

for j in range(n):
	po = a[j]
	if j - po < 0:
		ans[0] += 1
	else:
		ans[j-po] += 1
	if j + po + 1 <= n-1:
		ans[j+po+1] -= 1
for j in range(1,n):
	ans[j] += ans[j-1]
print(jo(ans))




