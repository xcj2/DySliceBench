import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():

    def main():
        
        N,K=map(int,input().split())
        D=set(map(int,input().split()))

        L={i for i in range(10)}
        U=L-D
        while True:

            sn = str(N)
            ln = len(sn)

            for i in range(ln):
                if int(sn[i]) not in U:
                    N+=1
                    break
                elif i==ln-1:
                    return int(N)
    print(main())



resolve()