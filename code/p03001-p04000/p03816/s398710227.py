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



mm = 1000000007
def solve ():
	t = 1
	for tt in range (t):
		n=nu()
		a=li()
		a.sort()
		mp={}
		for i in a:
			if(i in mp):
				mp[i]=mp.get(i)+1
			else:
				mp[i]=1
		i=0
		j=n-1
		cc=0
		while(i<j):
			if(mp.get(a[i])==1):
				i+=1
				continue
			if(mp.get(a[j])==1):
				j-=1
				continue
			cc+=2
			mp[a[i]]=mp.get(a[i])-1
			mp[a[j]]=mp.get(a[j])-1
			i+=1
			j-=1
		print(n-cc)
solve()
