import io, sys, atexit, os

import math as ma
from sys import exit
from decimal import Decimal as dec
from itertools import permutations


def li ():
	return list (map (int, input ().split ()))


def num ():
	return map (int, input ().split ())


def nu ():
	return int (input ())


def find_gcd ( x, y ):
	while (y):
		x, y = y, x % y
	return x


mm = 1000000007



def solve ():
	t = 1
	for it in range (t):
		n,m,c=num()
		b=li()
		cc=0
		for i in range(n):
			a=li()
			ss=c
			for j in range(m):
				ss+=a[j]*b[j]
			if(ss>0):
				cc+=1
		print(cc)





if __name__ == "__main__":
	solve ()