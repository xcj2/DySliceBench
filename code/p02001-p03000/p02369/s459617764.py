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

def Topo_sort(x,y):
	co = cl.Counter(n for m in x.values() for n in m)
	S = cl.deque([i for i in range(y) if co[i] == 0])
	while S:
		n = S.popleft()
		yield n
		for i in x[n]:
			co[i] -= 1
			if co[i] <= 0:
				S.append(i)
	if sum(co.values()) != 0:
		print(1)
		exit()
	else:
		print(0)
		exit()
# g = cl.dafaultdict(set)に有向グラフを作成し(g[~] != ~) リストが帰ってくる

v,e = m()

g = cl.defaultdict(set)

for i in range(e):
	s,t = m()
	g[s] |= {t}
a = list(Topo_sort(g,v))

