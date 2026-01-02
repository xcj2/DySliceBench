import sys
input = sys.stdin.readline
input = sys.stdin.buffer.readline

def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))


def main():
    N = II()
    A= LI()
    ans = 0

    for i in range(N):
        if A[i] % 2 == 0:
            if A[i]%3!=0 and A[i]%5!=0:
                ans += 1
                break

    if ans == 0:
        print("APPROVED")
    else:
        print("DENIED")




if __name__ == "__main__":
	main()