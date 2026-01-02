# -*- coding: utf-8 -*-

def main():
    n = int(input())
    li = dp(n)
    print(li[n])

def dp(n):
    inf=float('inf')
    dp = [inf for i in range(n+1)]
    dp[0] = 0
    money_list = get_money_list()
    for i in range(1, n + 1):
        for pay in money_list:
            if pay > i:
                continue
            else:
                dp[i] = min(dp[i - pay] + 1, dp[i])
    return dp

def create_list(n):
    i = 1
    money_list = []
    while i < 100000:
        money_list.append(i)
        i = i * n
    return money_list

def get_money_list():
    li = create_list(9)
    li.extend(create_list(6))
    li = list(set(li))
    li.sort(key=int, reverse=True)
    return li

if __name__ == '__main__':
    main()