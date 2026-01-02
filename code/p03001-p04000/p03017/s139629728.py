import sys,collections as cl,bisect as bs
sys.setrecursionlimit(100000)
Max = sys.maxsize
def l():
	return list(map(int,input().split()))
def m():
	return map(int,input().split())
def s(x):
	a = []
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
def jo(x):
	return " ".join(map(str,x))

n,a,b,c,d = m();
ss = list(input())
if c < d:
	k = s(ss[b-1:d])
	for i in range(len(k)):
		if k[i][0] == "#" and k[i][1] >= 2:
			print("No")
			exit()
	k = s(ss[a-1:c])
	for i in range(len(k)):
		if k[i][0] == "#" and k[i][1] >= 2:
			print("No")
			exit()
	print("Yes")
	exit()
else:
	# c > d
	count = 0
	k = s(ss[b-2:d])
	for i in range(len(k)):
		if k[i][0] == "#" and k[i][1] >= 2:
			print("No")
			exit()
		if k[i][0] == "." and k[i][1] >= 3:
			count = 1
	if count == 1:
		k = s(ss[a-1:c])
		for i in range(len(k)):
			if k[i][0] == "#" and k[i][1] >= 2:
				print("No")
				exit()
		print("Yes")
		exit()
	else:
		ss[d-1] = "#"
		k = s(ss[a-1:c])
		for i in range(len(k)):
			if k[i][0] == "#" and k[i][1] >= 2:
				print("No")
				exit()
		print("Yes")
		exit()
