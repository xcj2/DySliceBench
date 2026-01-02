import sys,collections as cl,bisect as bs,math,heapq as hq
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

def LIS(L):
  L = L[::-1]
  LIS=[]
  for i in L:
    pos = bs.bisect_right(LIS,i) 
    if len(LIS) <= pos:
      LIS.append(i)
    else:
      LIS[pos]=i
  return len(LIS)

n = onem()

a = []
c = 0
for i in range(n):
	a.append(onem())


print(LIS(a))
