import bisect
import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N=ii()
    L=list(mi())

    ans = 0
    L.sort()
    for ai in range(N):
        for bi in range(ai+1,N):
            a,b = L[ai],L[bi]

            left = bisect.bisect_left(L,abs(a-b)+1)
            right = bisect.bisect_right(L,a+b-1)

            count = right - left

            if left <= ai <= right:
                count -= 1

            if left <= bi <= right:
                count -= 1
            
            ans += count
            # if count > 0:
            #     print(a,b,count) 
            

    print(ans//3)


if __name__ == "__main__":
    main()