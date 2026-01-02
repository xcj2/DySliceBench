import sys

#+++++

def compute_cc(a_ll):
	cp=False
	ccc=0
	for pre_c, c in zip(a_ll,a_ll[1:]):
		if cp == True:
			cp = False
			continue
		elif pre_c == c:
			cp=True
			ccc+=1
	return ccc	




def main():
	s = input()
	k = int(input())
	
	if len(s)==1:
		return k//2
	
	if len(s)==2:
		if s[0]==s[1]:
			return k
		else:
			return 0
	
	first_diff=None
	i=0
	for pre_c, c in zip(s,s[1:]):
		i+=1
		if pre_c != c and first_diff is None:
			first_diff=i
			#pa(i)
	
	if first_diff is None:
		return len(s) * k // 2
		
	
	#len(s)>=3
	pp=s[:first_diff]
	nn=s[first_diff:]
	nc=nn+pp
	a=0
	a+=compute_cc(pp)
	a+=compute_cc(nc)*(k-1)
	a+=compute_cc(nn)
	print(a)
	
	
#+++++
isTest=False

def pa(v):
	if isTest:
		print(v)

if __name__ == "__main__":
	if sys.platform =='ios':
		sys.stdin=open('inputFile.txt')
		isTest=True
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)