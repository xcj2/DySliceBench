#-------------------------------------------------------------------
import sys
def p(*_a):
  _s=" ".join(map(str,_a))
  #print(_s)
  sys.stderr.write(_s+"\n")
#-------------------------------------------------------------------
N, K = map(int, input().split())			# "5 7" -> ["5", "7"] -> 5, 7 => N=5,K=7
R,S,P = map(int, input().split())		# 5 7 2
T = input()

def score(s):
	if s=='r': return P
	if s=='s': return R
	if s=='p': return S
	return 0

X=[""]*K
for i in range(K):
	X[i]=T[i::K]

p(X)

def max_score(x):
	a=0
	c=''
	A=x
	for s in A:
		if c==s:
			c=''
		else:
			a+=score(s)
			c=s

	#B=x[1:]+x[0]
	#b=0
	#c=''
	#for s in B:
	#	if c==s:
	#		c=''
	#	else:
	#		b+=score(s)
	#		c=s
	
	#p("A,a=", A,a)
	#p("B,b=", B,b)
	#return max(a,b)
	return a
	
	

ANS=[0]*K
for i,x in enumerate(X):
	ANS[i] = max_score(x)

ans=sum(ANS)
print(ans)
