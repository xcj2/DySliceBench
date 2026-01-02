import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))



def main():
    X,Y,Z,K=mi()
    A,B,C=list(mi()), list(mi()), list(mi())
    
    W = []
    for i in range(X):
        for j in range(Y):
            W.append(A[i]+B[j])

    W.sort(reverse=True)

    ans = []
    for w in W[:K]:
        for c in C:
            ans.append(w+c)
    
    ans.sort(reverse=True)
    print(*ans[:K],sep='\n')


if __name__ == "__main__":
    main()