import sys
input = sys.stdin.readline
input = sys.stdin.buffer.readline

def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))
def RN(N): return [input().strip() for i in range(N)]

def a(A,B,x): return (A*x//B)-A*(x//B)

def main():
    A,B,N = MI()
    """
    max = 0
    m = 0
    for x in range(0, N+1):
        ai = a(A,B,x)
        if max < ai :
            max = ai
        elif ai<0 and m == 0:
            max = ai
            m +=1

        print(x,a(A,B,x))
    """
    if N >= B:
        x = (N//B)*B-1
    elif N == B:
        x = N-1
    elif N < B:
        x = N
    print(a(A,B,x))

    



    


if __name__ == "__main__":
	main()