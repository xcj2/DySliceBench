# coding: utf-8
#-------------------------------------------------------------------
#-------------------------------------------------------------------
import sys
def p(*a):
  s=" ".join(map(str,a))
  #print(s)
  sys.stderr.write(s+"\n")
#-------------------------------------------------------------------
import math
def prm(n, r):
	return math.factorial(n)//math.factorial(n-r)

def cmb(n, r):
	return prm(n, r)//math.factorial(r)
#-------------------------------------------------------------------
def v(k):
	#p("B-1, k-1, cmb", B-1, k-1, cmb(B-1, k-1))
	p("R, k, cmb(R, k)",R, k, cmb(R, k))
#-------------------------------------------------------------------
MOD = 10**9+7
#-------------------------------------------------------------------


N, K = map(int, input().split())			# "5 7" -> ["5", "7"] -> 5, 7 => N=5,K=7

B=K
R=N-K


def calc(i):
	r = cmb(R+1, i)
	b = cmb(B-1, i-1)
	return (r * b) % MOD

for i in range(1,K+1):
	if R+1>=i:
		print( calc(i) )
	else:
		# R<=i, i>=R
		print(0)


