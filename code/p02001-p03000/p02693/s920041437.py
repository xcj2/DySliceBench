import sys
input = sys.stdin.readline
input = sys.stdin.buffer.readline

def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))
def RN(N): return [input().strip() for i in range(N)]


def main():
    K = II()
    A,B = MI()
    ans = 0

    for i in range(A, B+1):
        if i % K == 0:
            ans= 1
    if ans == 1:
        print("OK")
    else:
        print("NG")


if __name__ == "__main__":
	main()