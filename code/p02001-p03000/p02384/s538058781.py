#ITP1_11_A

def west(d):
	tmp=d[4]
	d[4]=d[1]
	d[1]=d[3]
	d[3]=d[6]
	d[6]=tmp

def east(d):
	tmp=d[4]
	d[4]=d[6]
	d[6]=d[3]
	d[3]=d[1]
	d[1]=tmp

def north(d):
	tmp=d[1]
	d[1]=d[2]
	d[2]=d[6]
	d[6]=d[5]
	d[5]=tmp

def south(d):
	tmp=d[1]
	d[1]=d[5]
	d[5]=d[6]
	d[6]=d[2]
	d[2]=tmp

def spin(d):
	tmp=d[2]
	d[2]=d[3]
	d[3]=d[5]
	d[5]=d[4]
	d[4]=tmp

def kaiten(d, op):
	if   op == "W": west(d)
	elif op == "E": east(d)
	elif op == "N": north(d)
	elif op == "S": south(d)

def inputDice():
	return list(map(int,("-1 "+input()).split()))

def solveB(d,d1,d2):
	for op in list("NWWWN-"):
		for i in range(4):
			if(d[1]==d1 and d[2]==d2):
				return d[3]
			spin(d)
		kaiten(d,op)
	return None

d=inputDice()
solveB(d,1,2)

for i in range(int(input())):
	d1,d2=map(int,input().split())
	print(solveB(d,d1,d2))
