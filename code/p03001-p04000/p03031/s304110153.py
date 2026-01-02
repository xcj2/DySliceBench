import sys
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def II(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def SI(): return input()
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')

def main():
    N, M = LI()
    s_li = []
    for i in range(M):
        s_li.append(LI()[1:])
    p_li = LI()

    import itertools
    counter = 0
    for i in itertools.product([0,1], repeat=N):  # product of switches
        for s, p in zip(s_li, p_li): # for each lights
            if sum([i[num-1] for num in s])%2 != p:
                break
        else:
            counter += 1
    print(counter)

main()