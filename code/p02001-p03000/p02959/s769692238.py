def INT_(n): return int(n)-1
def MI(): return map(int, input().split())
def MF(): return map(float, input().split())
def MI_(): return map(INT_, input().split())
def LI(): return list(MI())
def LI_(): return [int(x) - 1 for x in input().split()]
def LF(): return list(MF())
def LIN(n: int): return [I() for _ in range(n)]
def LLIN(n: int): return [LI() for _ in range(n)]
def LLIN_(n: int): return [LI_() for _ in range(n)]
def LLI(): return [list(map(int, l.split())) for l in input()]
def I(): return int(input())
def F(): return float(input())
def ST(): return input().replace('\n', '')


def main():
    N = I()
    A = LI()
    B = LI()

    total = 0

    res = 0
    for i in range(N):
        monster = max(0, A[i] - res)
        if res + B[i] <= A[i]:
            total += B[i] + res
            res = 0
        else:
            total += A[i]
            res = B[i] - monster
    total += min(res, A[N])
    print(total)


if __name__ == '__main__':
    main()
