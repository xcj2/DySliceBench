n,m,k = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
import random
import bisect

#n,m,k = random.randint(1,1000),random.randint(1,1000),random.randint(1,10**8)
##a = [random.randint(1,10**5) for i in range(n)]
#b = [random.randint(1,10**5) for i in range(m)]

def solv():
	global a,b,n,m,k
	akari = [0]*(n+1)
	bkari = [0]*(m+1)
	for i in range(n):
		akari[i+1] = akari[i] + a[i]

	for i in range(m):
		bkari[i+1] = bkari[i] + b[i]

	def bin(ls,s,e,sikii):
		if e - s <= 1:
			return s
		mid = (s+e)//2
		if sikii < ls[mid]:return bin(ls,s,mid,sikii)
		else:return bin(ls,mid,e,sikii)

	ans = 0
	for i in range(n+1):
		time = akari[i]
		if k - time < 0:break
		#ref = bin(bkari,0,m+1,k-time)
		ref = bisect.bisect_right(bkari,k-time)
		ans = max(ans,ref+i)
	return ans

def karisolv():
	global a,b,n,m,k
	akari = [0]*(n+1)
	bkari = [0]*(m+1)
	for i in range(n):
		akari[i+1] = akari[i] + a[i]

	for i in range(m):
		bkari[i+1] = bkari[i] + b[i]

	ans = 0
	for i in range(n+1):
		time = akari[i]
		ref = 0
		if k - time <= 0:break
		cost = 0
		for j in range(m+1):
			if k - time - bkari[j] >= 0:
				ans = max(ans,j+i)
		
	return ans

def makedata():
	global a,b,n,m,k
	n,m,k = random.randint(1,10000),random.randint(1,10000),random.randint(1,1000000)
	a = [random.randint(1,10**5) for i in range(n)]
	b = [random.randint(1,10**5) for i in range(m)]
import sys
def main():
	for i in range(1000000):
		makedata()
		kari = karisolv()
		kotae = solv()
		if kari != kotae:
			print(n,m,k,a,b)
			sys.exit()
print(solv()-1)