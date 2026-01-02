from sys import stdin, stdout # only need for big input

MOD = int(1e9+7)

def pow_mod(a , p , m):
    if p < 2:
        ans = 1
        for _ in range(p):
            ans *= a
            if ans >= m:
                ans = ans % m
        return ans
    ans = pow_mod(a , p //2 , m)
    ans = ans * ans

    if ans >= m :
        ans = ans % m
    if p % 2 :
        ans = ans * a 
        if ans >= m :
            ans = ans % m 
    return ans

    

def solve():
    n = int(input())
    A = [int(inp) for inp in input().split()]
    count_1 = [0] * 61 
    pow_2 = [pow_mod(2, i, MOD) for i in range(61)]
    for a in A :
        x = a
        while x :
           for i in range(61):
               if x & 1 :
                   count_1[i] += 1
               x = x >> 1
    # print(count_1)
    # print(pow_2)
    sum = 0
    # print(len(pow_2))
    # print(len(count_1))
    # for a in A:
    #     x = a
    #     while x :
    #         for i in range(61):
    #             # print(i)
    #             if x & 1:
    #                 sum += pow_2[i] * (n - count_1[i])
    #             else:
    #                 sum += pow_2[i] * (count_1[i])

    #             if sum >= MOD:
    #                 sum = sum % MOD
    #             x = x >> 1 
    for i in range(61):
        sum += pow_2[i] * count_1[i] * ( n - count_1[i])
        if sum >= MOD:
            sum = sum % MOD
    # print(sum)
    #sum = (sum * pow_mod(2, MOD - 2, MOD) ) % MOD
    print(sum)


def main():
    solve()


if __name__ == "__main__":
    main()