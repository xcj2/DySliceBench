def main():
    N = int(input())

    if N == 1:
        print(0)
    else:
        def prime_list(n):
            prime = [True for _ in range(n+1)]
            prime[0] = False
            prime[1] = False
            for i in range(2,int(n**0.5)+1):
                if not prime[i]:
                    continue
                for j in range(i*2,n+1,i):
                    prime[j] = False
            return [i for i in range(n+1) if prime[i]]

        prime_list = prime_list(N//2)
        cnt_list = [0 for _ in range(len(prime_list))]
        for i in range(len(prime_list)):
            count = 0
            d = N
            while d >= 1:
                count += d//(prime_list[i])
                d //= prime_list[i]
            cnt_list[i] = count

        def num(X):
            return len(list(filter(lambda x:x>=X-1,cnt_list)))

        print(num(75)+num(15)*(num(5)-1)+num(25)*(num(3)-1)+\
            num(5)*(num(5)-1)*(num(3)-2)//2)

if __name__ == "__main__":
    main()