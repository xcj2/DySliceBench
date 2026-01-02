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
	N,A,B = map(int, input().split())
	#S = input().rstrip()
	#vA = list(map(int, input().split()))
	#vX = [input().rstrip() for _ in [0,]*N]
	
	C = A+B

	res = 0
	
	if N<C:
		res = min(A,N)
	else:
		res = (N//C) * A
		res += min(N%C, A)
	
	#res = "No" if (S=="AAA" or S=="BBB") else "Yes"
	#res = -(-N//M)
	#res = gcd(N,M)
	print(res)
	
if __name__ == "__main__":
    main()
