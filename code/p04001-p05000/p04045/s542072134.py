import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():

    N,K=map(int,input().split())
    N= str(N)

    S={i for i in range(10)}
    D=set(map(int,input().split()))
    D=S-D

    def search(N):
        for i in range(len(N)):
            if int(N[i]) not in D:
                return True
            elif i==len(N)-1:
                return False

    while True:
        if search(N) ==True:
            N=str(int(N)+1)
        else:
            print(N)
            break









resolve()