import sys
sys.setrecursionlimit(1000000)
def main():
    N, X = (int(_) for _ in input().split())

    ex2 = []
    num = 1
    for i in range(51):
        ex2.append(num)
        num *= 2

    def Height(L):
        return 4 * ex2[L] - 3

    def TotalPatty(L):
        return 2 * ex2[L] - 1

    def NumPatty(L, x):
        M = Height(L)
        m = (M+1)//2
        if x == 1:
            if L == 0: return 1
            else: return 0
        elif x == m: return TotalPatty(L-1) + 1
        elif x == M: return 2*TotalPatty(L-1) + 1
        elif 1 < x < m: return NumPatty(L-1, x-1)
        else: return TotalPatty(L-1) + 1 + NumPatty(L-1, x-(Height(L-1)+2))

    print(NumPatty(N, X))
    return

if __name__ == '__main__':
    main()
