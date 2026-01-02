import sys

#+++++

def count_ab(a_s):
	ret=0
	is_a=False
	for c in a_s:
		if c == 'A':
			is_a=True
		elif is_a and c == 'B':
			ret+=1
			is_a=False
		else:
			is_a=False
	return ret
		
def main():
	n=int(input())
	sl=[]
	ret=0
	n_top_b=0
	n_buttom_a=0
	n_tb_ab=0
	
	for i in range(n):
		aa = input()
		ret+=count_ab(aa)
		if aa[0]=='B':
			n_top_b+=1
		if aa[-1]=='A':
			n_buttom_a+=1
		if aa[0]=='B' and aa[-1]=='A':
			n_tb_ab+=1
	
	min_n_ab=min(n_buttom_a, n_top_b)
	if min_n_ab == 0:
		return ret
	
	ret += min_n_ab
	if n_buttom_a==n_top_b and n_top_b==n_tb_ab:
		ret -= 1
	
	return ret
	
	
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
		
