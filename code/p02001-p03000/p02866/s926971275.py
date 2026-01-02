import io, sys, atexit, os
import math as ma
from sys import exit
from decimal import Decimal as dec
from itertools import permutations
from itertools import combinations


def li ():
	return list (map (int, sys.stdin.readline ().split ()))


def num ():
	return map (int, sys.stdin.readline ().split ())


def nu ():
	return int (input ())


def find_gcd ( x, y ):
	while (y):
		x, y = y, x % y
	return x


def lcm ( x, y ):
	gg = find_gcd (x, y)
	return (x * y // gg)



mm = 998244353
def solve ():
	t = 1
	for tt in range (t):
		n=nu()
		a=li()
		if (a [ 0 ] != 0):
			print (0)
			continue
		a.sort()
		if(a[0]!=0):
			print(0)
		else:
			ox=[]
			cc=1
			las=a[0]
			for i in range(1,n):
				if(las==a[i]):
					cc+=1
				else:
					ox.append((las,cc))
					cc=1
					las=a[i]
			ox.append ((las, cc))
			if(ox[0][1]!=1):
				print(0)
				continue
			last=ox[0][1]
			next=ox[0][0]+1
			ans=1
			for i in range(1,len(ox)):
				if(next!=ox[i][0]):
					ans=0
				ans=(ans*pow(last,ox[i][1],mm))%mm
				last=ox[i][1]
				next+=1
			print(ans)










if __name__ == "__main__":
	solve ()