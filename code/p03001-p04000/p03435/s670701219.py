def II(): return int(input())
def MI(): return map(int,input().split())
def LMI(): return list(map(int,input().split()))
def LIIN(n): return list(int(input()) for _ in range(n))
def LMIN(n): return [list(map(int, input().split())) for _ in range(n)]
def IS(): return input()
def MS(): return map(str,input().split())
def LMS(): return list(map(str,input().split()))
def LISN(n): return list(input() for _ in range(n))
def LMSN(n): return [input().split() for _ in range(n)]
MOD = 10**9+7
INF = 10**18

def main():
    x = [0] * 3
    y = [0] * 3
    a = LMIN(3)

    x[0] = 0
    for i in range(3):
        y[i] = a[0][i] - x[0]
    for i in range(3):
        x[i] = a[i][0] - y[0]

    for i in range(3):
        for j in range(3):
            if x[i]+y[j] != a[i][j]:
                print('No')
                return 0
    print('Yes')

if __name__ == '__main__':
    main()
