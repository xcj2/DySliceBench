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
    S = SI().strip()

    searching = 1
    count = [0]
    head = 0
    for i in range(N):
        if int(S[i]) == searching:
            count[head] += 1
        else:
            searching = (searching+1)%2
            head += 1
            count.append(1)
    if len(count)//2 <= K:
        print(N)
        sys.exit()

    count.append(0)

    current_sum = sum(count[0:2*K+1])
    max_length = current_sum
    try:
        for k in range(1, N):
            if 2*k+2*K > len(count): break
            current_sum = current_sum - count[2*k-2] - count[2*k-1] + count[2*k+2*K-1] + count[2*k+2*K]
            max_length = max(current_sum, max_length)
    except:
        pass
    print(max_length)

main()