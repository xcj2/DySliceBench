
def inputTable(a):
	lit=[]
	for aa in range(a):
		lit.append(list(map(int,input().split())))
	return lit

def kouten(dai):
	x=dai[0]
	dai[0]=dai[1]
	dai[1]=dai[5]
	dai[5]=dai[4]
	dai[4]=x
	return(dai)
def sokuten(dai):
	x=dai[0]
	dai[0]=dai[2]
	dai[2]=dai[5]
	dai[5]=dai[3]
	dai[3]=x
	return(dai)

def tokei(dai):
	dai1 = dai[1]
	dai[1] = dai[2]
	dai[2] = dai[4]
	dai[4] = dai[3]
	dai[3] = dai1
	return(dai)

def check(dai,daini):
	for j in range(4):
		if daini[0] == dai[0] and daini[1] == dai[1] and daini[2] == dai[2] and daini[3] == dai[3] and daini[4] == dai[4] and daini[5] == dai[5]:
			print('No')
			return True
		tokei(dai)
	return False

def checkup(a,b):
	for unuse in range(3):
		if not check(a,b):
			kouten(a)
		else:
			return True
		if not check(a,b):
			sokuten(a)
			if unuse==2 :
				if	not check(a,b) :
					return	False  
		else:
			return True

n=int(input())
daise=inputTable(n)
k=0
R=0
for cc in range(n):
	if k==1:
		break
	for dd in range(cc+1,n):
		if k==1:
			break
		if   checkup(daise[cc],daise[dd]):
			k=1
			break
		
if k==R:
	print('Yes')
