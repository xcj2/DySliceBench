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
    N, K = MI()
    d = [0]*K
    A = [0]*K
    for i in range(K):
        d[i] = II()
        A[i] = LI()
    Alist = []
    for i in range(K):
        for j in range(d[i]):
            Alist.append(A[i][j])
    print(N-len(set(Alist)))


if __name__ == "__main__":
	main()