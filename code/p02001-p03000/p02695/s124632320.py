import itertools
import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N,M,Q=mi()
    X = []
    for i in range(Q):
        a,b,c,d = mi()
        X.append((a,b,c,d))

    ans = 0
    num_list = list(range(1,M+1))
    for _nums in itertools.combinations_with_replacement(num_list, N):
        nums = list(_nums)
        D = 0
        for j in range(Q):
            a,b,c,d = X[j]
            if nums[b-1] - nums[a-1] == c: 
                D += d
        
        ans = max(ans,D)

    print(ans)



if __name__ == "__main__":
    main()