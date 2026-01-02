import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))


INF=10**20
def main():
    N,K=mi()
    MOD = 10**9+7

    ans = 0
    dic = {} 
    for x in range(K,0,-1):  # gcd = x となるA1~AN(<=K)を探す
        p_count = K//x
        count = pow(p_count,N,MOD)

        i = 2
        while x*i <= K:
            if not x*i in dic: break
            count -= dic[x*i]
            count %= MOD
            i += 1

        count %= MOD
        dic[x] = count
        
        ans += count * x
        ans %= MOD
        # print(x,count)
    
    print(ans)








if __name__ == "__main__":
    main()