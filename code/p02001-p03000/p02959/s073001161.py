import sys,collections as cl,bisect as bs
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

b = l()

co = 0

if a[0] <= b[0]:
	co += a[0]
	nokori = b[0] - a[0]
	a[0] = 0
else:
	nokori = 0
	co = b[0]


for i in range(1,n):
	if nokori >= a[i]:
		co += a[i]
		nokori = b[i]
	else:
		if nokori + b[i] >= a[i]:
			co += a[i]
			nokori = b[i] + nokori - a[i]
		else:
			co += b[i] + nokori
			nokori = 0

if nokori >= a[-1]:
	co += a[-1]
else:
	co += nokori

print(co)









