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

def kaiten(d, op):
	if   op == "W": west(d)
	elif op == "E": east(d)
	elif op == "N": north(d)
	elif op == "S": south(d)
	else          : raise AssertionError()

def dump(d):
	print(" ".join(map(str,d)))

def inputDice():
	return list(map(int,("-1 "+input()).split()))

d=inputDice()
for op in list(input()):
	kaiten(d,op)
print(d[1])
