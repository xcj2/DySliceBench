def main():
    n ,m, x = map(int, input().split())
    c, a = [0 for i in range(n)], [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        c[i], *a[i] = [int(i) for i in input().split()]
    ans = solve(n, m, x, c, a)
    print(ans)


def solve(n, m, x, c, a):
    INF = 10 ** 9
    ans = INF
    for bits in range(2 ** n):
        cost, skill = 0, [0 for i in range(m)]
        #print(f'{bits=}')
        for i in range(n):
            bit = bits >> i & 1
            #print(f'{bit=}')
            if bit:
                cost += c[i]
                for j in range(m):
                    skill[j] += a[i][j]
        #print(skill)
        if judge(skill, x):
            ans = min(ans, cost)
    return -1 if ans == INF else ans

def judge(skill, x):
    for i in skill:
        if i < x:
            return False
    return True

if __name__ == '__main__':
    main()