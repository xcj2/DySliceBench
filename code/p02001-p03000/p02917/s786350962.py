import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N=ii()
    B=list(mi())

    X = []
    X.append(B[0])
    X.append(B[0])

    for i in range(1,N-1):
        last = X[-1]
        if last <= B[i]:
            X.append(B[i])
        else:
            X[-1] = B[i] 
            X.append(B[i])
    
    # print(X)
    print(sum(X))







if __name__ == "__main__":
    main()