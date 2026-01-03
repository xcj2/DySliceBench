MOD = 10**9+7

def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table

def mi():
    return map(int, input().split())

def main():
    N = int(input())
    dic = {}
    ans = 1
    for i in range(1, N+1):
        for v in prime_decomposition(i):
            if not v in dic:
                dic[v] = 0
            dic[v] += 1

    for v in dic.values():
        ans *= (v+1)
        ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()