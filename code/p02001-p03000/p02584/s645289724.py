import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    X,K,D=mi()

    if X == 0:
        ans = D if K % 2 == 1 else 0
        print(ans)
        exit()
    
    n = abs(X)//D
    ans = INF
    for n2 in [n-1,n,n+1]:
        m = K-n2

        if X > 0:
            res = X - D*n2
        else:
            res = X + D*n2

        if m <= 0:
            if X > 0:
                res = X - D*K
            else:
                res = X + D*K
            ans = min(ans,abs(res))
            continue


        if m % 2 == 1:
            res = min(abs(res + D), abs(res-D))
        else:
            res = res
        
        ans = min(ans,abs(res))
    
    print(ans)






if __name__ == "__main__":
    main()