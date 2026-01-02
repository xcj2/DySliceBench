import sys
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
	A,B = map(int, input().split())
	#S = input().rstrip()
	#vA = list(map(int, input().split()))
	#vX = [input().rstrip() for _ in [0,]*N]
	
	X = 0.08
	Y = 0.10
	
	res = 0
	for i in range(1, 1101):
		if int(i*X)==A and int(i*Y)==B:
			res = i
			break
	else:
		res = -1
	
	#res = "No" if (S=="AAA" or S=="BBB") else "Yes"
	#res = -(-N//M)
	#res = gcd(N,M)
	print(res)
	
if __name__ == "__main__":
    main()
