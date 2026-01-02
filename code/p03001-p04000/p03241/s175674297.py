import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N,M=mi()

    def divisors(n):
        res = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                res.append(i)
                if i != n // i:
                    res.append(n//i)

        return res

    D = divisors(M)
    ans = 1
    for d in D:
        X = M // d
        if X-N+1 > 0:
            ans = max(ans,d)
    
    print(ans)




if __name__ == "__main__":
    main()