# pythonっぽくなくてダサい
stops=[0,1,2,3,4,5,6,7,8,9,5,4,3,2,1]
istops=[[0],[1,14],[2,13],[3,12],[4,11],[5,10],[6],[7],[8],[9]]

def asloop(cur, end):
	result=[]
	for i in range(cur, cur+len(stops)):
		x=stops[i%len(stops)]
		result.append(x)
		if x==end:
			return	result

def asrecurse(cur, end, result=None):
	if result is None:
		result=[]
	x=stops[cur]
	result.append(x)
	next=(cur+1)%len(stops)
	if x==end:
		return	result
	return asrecurse(next, end, result)

def loop(start, end):
	result=[i for i in range(len(stops)+1)]
	for i in istops[start]:
		a=asloop(i, end)
		if len(a) < len(result):
			result=a
	return	result

nloop=int(input())
for i in range(nloop):
	inputs=input().split()
	result=loop(int(inputs[0]), int(inputs[1]))
	print(' '.join([str(x) for x in result]))
