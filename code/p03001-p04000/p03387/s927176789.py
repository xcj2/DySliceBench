import sys

count=0
l=list(map(int,input().split()))


def sousa1():
	global count
	global l
	x_min=l.index(min(l))
	x_max=l.index(max(l))
	x_else = 0 if x_min+x_max==3 else 1 if x_min+x_max==2 else 2
	count+=l[x_max]-l[x_else]

	l[x_min]+=l[x_max]-l[x_else]
	l[x_else]=l[x_max]
	

def sousa1_2():
	global count
	global l
	x_min=l.index(min(l))
	x_max=l.index(max(l))
	x_else = 0 if x_min+x_max==3 else 1 if x_min+x_max==2 else 2

	count+=1
	l[x_else]+=1
	l[x_max]+=1

def sousa2():
	global count
	global l
	x_min=l.index(min(l))
	x_max=l.index(max(l))
	count+=(l[x_max]-l[x_min])/2
	l[x_min]=l[x_max]


def judge():
	x_min=l.index(min(l))
	x_max=l.index(max(l))
	x_else = 0 if x_min+x_max==3 else 1 if x_min+x_max==2 else 2
	if l[x_max]!=l[x_else]:
		return 0
	elif (l[x_max]-l[x_min])%2==0:
		return 1
	else:
		return 2

while not(l[0]==l[1] and l[1]==l[2] and l[0]==l[2]):
	hoge=judge()
	if hoge==0:
		sousa1()
	elif hoge==1:
		sousa2()
	else:
		sousa1_2()

print(int(count))
