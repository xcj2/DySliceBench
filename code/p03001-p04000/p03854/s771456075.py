def extract_6(x):
	strtemp=' '
	if(len(x)>=6):
		temp=[0]*6
		for i in range(6):
			temp[i]=x[len(x)-6+i]
	else:
		temp='false'
	strtemp=''.join(temp)
	return(strtemp)

def extract_5(x):
	strtemp=' '
	if(len(x)>=5):
		temp=[0]*5
		for i in range(5):
			temp[i]=x[len(x)-5+i]
	else:
		temp='false'
	strtemp=''.join(temp)
	return(strtemp)
	
def extract_7(x):
	strtemp=' '
	if(len(x)>=7):
		temp=[0]*7
		for i in range(7):
			temp[i]=x[len(x)-7+i]
	else:
		temp='false'
	strtemp=''.join(temp)
	return(strtemp)

S=input()
flag=1
while(flag==1):
	if(extract_7(S)=='dreamer'):
		S=S[:-7]
	elif(extract_6(S)=='eraser'):
		S=S[:-6]
	elif(extract_5(S)=='dream'):
		S=S[:-5]
	elif(extract_5(S)=='erase'):
		S=S[:-5]
	else:
		flag=0
if len(S)!=0:
	print('NO')
else:
	print('YES')