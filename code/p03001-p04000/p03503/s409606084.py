def main():
    from sys import stdin
    def input():
        return stdin.readline().strip()

    def str_to_bool(i):
        if i == '0':
            return False
        else:
            return True

    n = int(input())
    f = [[str_to_bool(i) for i in input().split()] for _ in range(n)]
    p = [[int(i) for i in input().split()] for _ in range(n)]

    # full search
    from itertools import product

    ans = -float('inf')
    flag = True
    for iterator in product([False, True], repeat=10):
        if flag:
            flag = False
            continue

        profit = 0
        for store_ind in range(n):
            num = 0
            for i in range(10):
                if iterator[i] and f[store_ind][i]:
                    num += 1
            profit += p[store_ind][num]
        
        if ans < profit:
            ans = profit

    print(ans)

main()