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

a.sort()

mina = []

pra = []

for i in range(len(a)):
	if a[i] >= 0:
		pra.append(a[i])
	else:
		mina.append(a[i])

lp = len(pra)

lm = len(mina)
ans = 1
if lp == 0:
	if k % 2 != 0:
		for i in range(0,k,2):
			if i == k-1:
				i = -(1+i)
				ans *= mina[i]
			else:
				i = -(1+i)
				ans *= (mina[i]*mina[i-1]) % mod
			ans %= mod
		print(ans % mod)
	else:
		for i in range(0,k,2):
			ans *= (mina[i]*mina[i+1]) % mod
			ans %= mod
		print(ans % mod)
elif lp == 1:
	if n == k:
		ans *= pra[0]
		for i in range(0,lm,2):
			if i == lm-1:
				i = -(1+i)
				ans *= mina[i]
			else:
				i = -(1+i)
				ans *= (mina[i]*mina[i-1]) % mod
			ans %= mod
		print(ans % mod)
	else:
		if k % 2 == 0:
			for i in range(0,k,2):
				ans *= (mina[i]*mina[i+1]) % mod
				ans %=  mod
			print(ans % mod)
		else:
			ans *= pra[0] 
			for i in range(0,k-1,2):
				ans *= (mina[i]*mina[i+1]) % mod
				ans %=  mod
			print(ans % mod)
else:
	cp = lp-1
	cm = 0
	
	for _ in range(k):
		if cp != -1 and cm != lm:
			if abs(mina[cm]) <= pra[cp]:
				if cp == 0:
					if (k-lp) % 2 == 0:
						cp -= 1
					else:
						cm += 1
				else:
					cp -= 1
			else:
				if cm == lm-1:
					if lm % 2 == 0:
						cm += 1
					else:
						cp -= 1
				else:
					
					cm += 1
		elif cp != -1:
			cp -= 1
		elif cm != lm:
			cm += 1
			
		else:
			break
	if cm % 2 != 0:
		if cp == lp-1:
			cp -= 1
			cm -= 1

		else:
			if cp != -1 and cm != lm:
				if pra[cp]*pra[cp+1] <= -mina[cm]*-mina[cm-1]:
					cp += 1
					cm += 1
				else:
					cp -= 1
					cm -= 1
			elif cp != -1:
				cp -= 1
				cm -= 1
			elif cm != lm:
				cp += 1
				cm += 1

	ii = -2
	for i in range(0,cm,2):
		if i == cm-1:
			ii = i
			continue
		ans *= (mina[i] * mina[i+1]) % mod
		ans %= mod
	for i in range(lp-1,cp,-1):
		ans *= pra[i] % mod
		ans %= mod
	if ii == cm-1:
		ans *= mina[ii]
		ans %= mod

		
	print(ans)




