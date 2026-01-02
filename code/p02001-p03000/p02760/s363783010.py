def i():
    return int(input())
def i2():
    return map(int,input().split())
def s():
    return str(input())
def l():
    return list(input())
def intl():
    return list(int(k) for k in input().split())

a=[intl() for _ in range(3)]
n=i()
b=[int(input()) for _ in range(n)]
flag=0
falg=0
for i in range(3):
	for j in range(3):
		if a[i][j] in b:
			a[i][j]=0
for i in range(3):
	for j in range(3):
		if a[i][0]==0 and a[i][1]==0 and a[i][2]==0:
			flag+=1
		elif a[0][j]==0 and a[1][j]==0 and a[2][j]==0:
			flag+=1
		elif i==j and a[i][j]==0:
			falg+=1
			if falg==3:
				flag+=1
if a[0][2]==0 and a[1][1]==0 and a[2][0]==0:
	flag+=1
if flag>=1:
	print('Yes')
else:
	print('No')