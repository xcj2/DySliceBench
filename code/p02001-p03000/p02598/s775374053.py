import math
import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))


INF=10**20
def main():
    N,K=mi()
    A=list(mi())

    A.sort(reverse=True)
    l = 0
    r = A[0]

    while r-l > 1:
        # print("l,r:",l,r)
        mid = (r+l)//2
        
        count = 0

        for i in range(N):
            if mid < A[i]:
                count += math.ceil(A[i]/mid)-1
        
        # print(mid,count)
        if count > K:
            l = mid
        else:
            r = mid
    
    print(r)

    

if __name__ == "__main__":
    main()