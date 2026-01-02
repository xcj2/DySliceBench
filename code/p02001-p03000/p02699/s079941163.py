from math import *
from copy import *
from string import *				# alpha = ascii_lowercase
from random import *
from sys import stdin
from sys import maxsize
from operator import *				# d = sorted(d.items(), key=itemgetter(1))
from itertools import *
from collections import Counter		# d = dict(Counter(l))
import math

def bin1(l,r,k,t,b,val,ans):
	if(l>r):
		return ans
	else:
		mid=(l+r)//2
		v=k**mid
		if(v==val):
			return v
		elif(v>val):
			ans=mid
			return bin1(mid+1,r,k,t,b,val,ans)
		else:
			return bin1(l,mid-1,k,t,b,val,ans)
		
def bin2(l,r,k,t,b,val,ans):
	if(l>r):
		return ans
	else:
		mid=(l+r)//2
		v=t*(k**mid)+b*(mid)
		if(v==val):
			return v
		elif(v>val):
			ans=mid
			return bin2(l,mid-1,k,t,b,val,ans)
		else:
			return bin2(mid+1,r,k,t,b,val,ans)

def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    l=[]
    for i in range(2,n+1):
    	if(prime[i]):
    		l.append(i)
    return l
def bin(l,r,ll,val):
	if(l>r):
		return -1
	else:
		mid=(l+r)//2
		if(val>=ll[mid][0] and val<=ll[mid][1]):
			return mid
		elif(val<ll[mid][0]):
			return bin(l,mid-1,ll,val)
		else:
			return bin(mid+1,r,ll,val)
def deci(n):
	s=""
	while(n!=0):
		if(n%2==0):
			n=n//2
			s="0"+s
		else:
			n=n//2
			s="1"+s
	return s
def diff(s1,s2):
	if(len(s1)<len(s2)):
		v=len(s1)
		while(v!=len(s2)):
			s1="0"+s1
			v=v+1
	else:
		v=len(s2)
		while(v!=len(s1)):
			s2="0"+s2
			v=v+1
	c=0
	for i in range(len(s1)):
		if(s1[i:i+1]!=s2[i:i+1]):
			c=c+1
	return c
from sys import stdin, stdout 
def fac(a,b):
	v=a
	while(a!=b):
		v*=a-1
		a=a-1
	return v
def bino(l,r,n):
	if(l>r):
		return -1
	else:
		mid=(l+r)//2
		val1=math.log((n/mid)+1,2)
		val2=int(val1)
		if(val1==val2):
			return val1
		elif(val1<1.0):
			return bino(l,mid-1,n)
		else:
			return bino(mid+1,r,n)

def binary(l,r,ll,val,ans):
	if(l>r):
		return ans
	else:
		mid=(l+r)//2
		if(val%ll[mid]==0):
			ans=ll[mid]
			return binary(l,mid-1,ll,val,ans)
		else:
			return binary(l,mid-1,ll,val,ans)
def odd(n,ans,s):
	if(n%2!=0 or n in s):
		return ans
	else:
		s.add(n)
		return odd(n//2,ans+1,s)

if __name__ == '__main__':
	s,w=map(int,input().split(" "))
	if(w>s-1):
		print("unsafe")
	else:
		print("safe")