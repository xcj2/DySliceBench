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

p = l()

pp = p[:]
pp.sort()
if p == pp:
	print("YES")
	exit()

for i in range(n):
	for j in range(i+1,n):
		ppp = p[:]
		ppp[i],ppp[j] = ppp[j],ppp[i]
		if all(pp[k] == ppp[k] for k in range(n)):
			print("YES")
			exit()
else:
	print("NO")





