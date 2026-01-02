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

n,d = m()

a =[]
for i in range(n):
	a.append(l())
co = 0
su = 0
for i in range(n-1):
	for j in range(i+1,n):
		su = 0
		for k in range(d):
			su += (a[i][k] - a[j][k])**2
		if math.sqrt(su) == int(math.sqrt(su)):
			co += 1
print(co)

