import sys

#+++++

def is_tr(a,b,c):
	if a < b+c:
		return True
	return False


def main():
	n = int(input())
	ll = list(map(int, input().split()))
	n=len(ll)
	ll.sort(reverse = True)
	pa(ll)
	
	ret = 0
	for i,l1 in enumerate(ll[:-2]):
		for j, l2 in enumerate(ll[i+1:-1]):
			pa(ret)
			if not is_tr(l1, l2, ll[j+1]):
				break
			if is_tr(l1,l2,ll[-1]):
				pa('ggg')
				ret += n-(i+1+j+1)
				continue
			ok=i+j+1
			ng=n-1
			while ng-ok > 1:
				mid = (ok+ng)//2
				if is_tr(l1,l2,ll[mid]):
					ok =mid
				else:
					ng = mid
			pa((ok,j+i+1))
			ret += (ok - (i+j+1))
	
	print(ret)
	
	
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