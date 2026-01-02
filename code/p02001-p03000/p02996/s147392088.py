import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7

def main(): 
    N = II()
    AB = []
    for _ in range(N):
        AB.append(LI())

    # Bi の小さい順（締切の早い順）にソート O(NlogN)
    AB.sort(key=lambda x: x[1])

    current_time = 0
    for i in AB:
        current_time += i[0]
        if current_time > i[1]:
            print('No')
            return
    print('Yes')


main()