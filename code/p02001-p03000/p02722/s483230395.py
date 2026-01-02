import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N=ii()

    def divisors(n):
        res = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                res.append(i)
                if i != n // i:
                    res.append(n//i)

        return res

    ans = 0
    ans += len(divisors(N-1)) - 1

    for k in divisors(N)[1:]:
        n = N
        while n % k == 0:
            n //= k
        if n % k == 1:
            ans += 1
    
    print(ans)




if __name__ == "__main__":
    main()