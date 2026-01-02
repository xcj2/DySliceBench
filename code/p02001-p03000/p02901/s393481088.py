import sys

sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return list(map(int, sys.stdin.readline().split()))
def II(): return int(sys.stdin.readline())
def LS(): return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]




def change(iter, org):
    return sum([org[i-1] for i in iter])

def main():
    n, m = LI()
    cs = []
    a_s = []
    b_s = []
    org = [2**i for i in range(n)]
    for i in range(m):
        a, b = LI()
        a_s.append(a)
        b_s.append(b)
        cs.append(change(LI(), org))

    mem = [[INF for i in range(2**n)] for i in range(m)]

    mem[0][0] = 0
    mem[0][cs[0]] = a_s[0]

    for i in range(1, m):
        mem[i][0] = 0
        for j in range(2**n):
            mem[i][j] = mem[i-1][j]
        for j in range(2**n):
            if mem[i-1][j] != INF:
                # print("MWM", i, j | cs[i], j, cs[i])

                mem[i][j | cs[i]] = min(a_s[i] + mem[i-1][j], mem[i][j | cs[i]])
                # print("NAN", a_s[i] + mem[i-1][j], mem[i-1][j | cs[i]], mem[i-1][j], a_s[i], mem[i][j | cs[i]])
        # print(mem[i][15])
    # print(mem)
    print(mem[-1][-1] if mem[-1][-1] != INF else "-1")



if __name__ == '__main__':
    main()