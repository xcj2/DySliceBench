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
    N, M = MI()
    H = LI()
    H.insert(0,0)
    A = [0]*M
    B = [0]*M
    ans = 0
    for i in range(M):
        A[i], B[i]=MI()

    Hnum = [0]*(N+1)
    Hnum[0] = 1

    for i in range(M):
        if H[A[i]]>H[B[i]]:
            Hnum[B[i]]+=1
        elif H[A[i]]<H[B[i]]:
            Hnum[A[i]]+=1
        elif H[A[i]]==H[B[i]]:
            Hnum[A[i]]+=1
            Hnum[B[i]]+=1
    print(Hnum.count(0))


    """
    for i in range(1,N+1):
        ng = 0
        for j in range(M):
            if A[j] == i:
                if H[i]<=H[B[j]]:
                    ng += 1
                    break
            if B[j] == i:
                if H[i]<=H[A[j]]:
                    ng += 1
                    break
        if ng == 0:
            ans += 1
    print(ans)"""


    


if __name__ == "__main__":
	main()