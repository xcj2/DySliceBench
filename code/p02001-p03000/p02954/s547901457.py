import sys

#+++++


def gh(n):
	return n // 2 + n % 2
	
def gn(n):
	return  n // 2
			
def main():
	l = list(input())
	ret = [0 for _ in l]
	n=len(l)
	
	p='L'
	count=0
	for i, (c, nc) in enumerate(zip(l,l[1:])):
		if p=='L' and c == 'R':
			count=0
		
		if c == 'R' and nc == 'L':
			count+=1
			#print(count)
			ret[i]+=gh(count)
			ret[i+1]+=gn(count)
			#print(ret)
			p='R'
		elif c == 'R':
			p='R'
			count+=1
			#print(ret)
		else:
			p='L'
	
	p='R'
	count=0
	for i, (c, nc) in enumerate(zip(l[-1::-1],l[-2::-1])):
		#print(c,nc,i)
		if p=='R' and c == 'L':
			count=0
		
		if c == 'L' and nc == 'R':
			count+=1
			ret[n-i-1]+=gh(count)
			ret[n-i-2]+=gn(count)
			#print(ret)
			p='L'
		elif c == 'L':
			p='L'
			count+=1
		else:
			p='R'
	
	ret=' '.join([str(i) for i in ret])
	print(ret)
	
#+++++

if __name__ == "__main__":
	if sys.platform =='ios':
		sys.stdin=open('inputFile.txt')
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)