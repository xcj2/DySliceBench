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
    A = LI()
    BandC = []
    for i in range(M):
        BandC.append(LI())
 
    A = sorted(A)
    BandC = sorted(BandC, key=lambda x: x[1], reverse=True)
 
    BandC_counter = 0
    BandC_position = 0
    BandC_sum = 0
    for A_position in range(N):
        if A[A_position] > BandC[BandC_position][1]:
            break
        BandC_sum += BandC[BandC_position][1]
        BandC_counter += 1
        if BandC_counter >= BandC[BandC_position][0]:
            BandC_position += 1
            BandC_counter = 0
            if BandC_position >= len(BandC):
                A_position += 1
                break
    else:
        A_position += 1
 
    print(BandC_sum + sum(A[A_position:]))

main()