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
    N, K = LI()
    V_li = LI()

    maximum = 0
    for take_count in range(min(K+1, N)):
        for take_left in range(take_count+1):
            # if take_left > N: break
            took = V_li[:take_left] + ([] if take_count == take_left else V_li[-(take_count - take_left):])
            took = sorted(took)
            for trash_count in range(K - take_count):
                if took and took[0] < 0:
                    took.pop(0)
                else:
                    break
            if not took:  # empty
                 took = [0]
            # print(took)
            maximum = max(maximum, sum(took))
    if N==1:
        maximum = max(0, V_li[0])
    if K >= N:
        maximum = max(maximum, sum(V_li))

    print(maximum)


main()