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

def equal(da, db):
	for op in list("NWWWN-"):
		for i in range(4):
			if(da[1]==db[1] and da[2]==db[2] and da[3]==db[3] and da[4]==db[4] and da[5]==db[5] and da[6]==db[6]):
				return True
			spin(db)
		kaiten(db,op)
	return False

da=inputDice()
db=inputDice()
if equal(da,db):
	print("Yes")
else:
	print("No")

