import sys,collections as cl,bisect as bs,math
sys.setrecursionlimit(100000)
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
		if aa == x[i+1]:
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

n = onem()

a = l()
k = 0
for i in range(n):
	if a[-(i+1)] == 1:
		k = n - i
		break

m = [0 for i in range(k+1)]
al = 0
for i in range(k,0,-1):
	co = 0
	if k // i < 2:
		m[i] = a[i-1]
		al += a[i-1]
	else:
		if i != 1:
			for j in range(1,k // i):
				co += m[i * (j+1)]
				co %= 2
			m[i] = (co ^ a[i-1])
			al += m[i]
		else:
			al %= 2
			m[1] = (al ^ a[0])

print(sum(m))
kkkk = []

for i in range(len(m)):
	if m[i] == 1:
		kkkk.append(i)
if len(kkkk) != 0:
	print(jo(kkkk))


