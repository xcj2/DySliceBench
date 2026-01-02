import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")

def main():
    def parity_onebit(x):
        return bin(x).count("1") & 1

    def make_route(s, g, state):
        if state.count(-1) == 1:
            return [s, g]
        sep_dig = bin(s ^ g)[::-1].find("1")
        s_bit = (s >> sep_dig) & 1
        Lstate = state[:]
        Rstate = state[:]
        Lstate[sep_dig] = s_bit
        Rstate[sep_dig] = 1 - s_bit
        for i in range(16):
            ng = 0
            i_copy = i
            for sk in Lstate[::-1]:
                ng <<= 1
                if sk == -1:
                    ng += i_copy & 1
                    i_copy >>= 1
                else:
                    ng += sk
            ns = ng ^ (1 << sep_dig)
            if ng != s and parity_onebit(ng) != parity_onebit(s) and ns != g:
                break
        res = make_route(s, ng, Lstate)
        state[sep_dig] = 1 - s_bit
        res += make_route(ns, g, Rstate)
        return res

    n, s, g = map(int, input().split())
    if parity_onebit(s) == parity_onebit(g):
        print("NO")
        exit()
    ans=make_route(s, g, [-1] * n)
    print("YES")
    print(*ans)
    #print(*[format(a,"b").zfill(n) for a in ans])

main()
