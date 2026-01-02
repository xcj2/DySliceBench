import sys
#from collections import deque as dq
input = sys.stdin.readline

def gcd(a: int, b: int):
    """ https://cocodrips.hateblo.jp/entry/2014/03/05/143623
    """
    while b:
        a, b = b, a%b
    return a

def lcm(a: int, b: int):
    return a * b // gcd(a, b)


def main():
	#N,A,B = map(int, input().split())
	S = input().rstrip()
	Q = int(input())
	#vA = list(map(int, input().split()))
	#vX = [input().rstrip() for _ in [0,]*N]
	
	rev = 0		# reverse
	
	DF = "" #dq([]) # reversed Head!!
	DR = "" #dq([])
	for q in range(Q):
		tq = input().split()
		if tq[0]=="1":
			rev ^= 1
		else:
			T,F,C = tq
			if F=="1":
				# C to top
				if rev == 0:
					DF += C #DF.appendleft(C) 
				else:
					DR += C #DR.append(C)
			else:
				# C to bottom
				if rev == 0:
					DR += C #DR.append(C)
				else:
					DF += C #DF.appendleft(C)	
	
	
	if rev == False:
		res = DF[::-1] + S + DR
	else:
		res = DR[::-1] + S[::-1] + DF

	print(res)
	
if __name__ == "__main__":
    main()
